from pathlib import Path
import argparse
import csv
import json
import logging
import xml.etree.ElementTree as ET
import requests
from io import StringIO

BASE_URL = "https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test"
GROUP_NUMBER = "0"

def setup_logger(last_name: str) -> logging.Logger:
    logger = logging.getLogger("qa_tasks")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))

    fh = logging.FileHandler(f"json__{last_name}.log", encoding="utf-8")
    fh.setLevel(logging.ERROR)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger


def task_csv_from_github(last_name: str, logger: logging.Logger):
    csv_urls = [
        f"{BASE_URL}/work_with_csv/random.csv",
        f"{BASE_URL}/work_with_csv/random-michaels.csv",
    ]
    rows = []
    seen = set()
    header = None

    for url in csv_urls:
        try:
            r = requests.get(url)
            r.raise_for_status()
            reader = csv.reader(StringIO(r.text))
            file_header = next(reader, None)
            if header is None:
                header = file_header
            elif file_header != header:
                logger.info(f"Попередження: заголовки у {url.split('/')[-1]} відрізняються.")
            for row in reader:
                t = tuple(row)
                if t not in seen:
                    seen.add(t)
                    rows.append(row)
        except Exception as e:
            logger.error(f"Не вдалося завантажити {url}: {e}")

    out_path = Path(f"result_{last_name}.csv")
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        if header:
            writer.writerow(header)
        writer.writerows(rows)

    logger.info(f"Завдання 1: створено {out_path.name}; рядків без дублікатів: {len(rows)}.")
    return out_path


def task_json_from_github(logger: logging.Logger):
    json_urls = [
        f"{BASE_URL}/work_with_json/localizations_en.json",
        f"{BASE_URL}/work_with_json/localizations_ru.json",
        f"{BASE_URL}/work_with_json/login.json",
        f"{BASE_URL}/work_with_json/swagger.json",
    ]
    invalid = 0
    for url in json_urls:
        try:
            r = requests.get(url)
            r.raise_for_status()
            json.loads(r.text)
        except Exception as e:
            invalid += 1
            logger.error(f"{url.split('/')[-1]}: {e}")

    if invalid == 0:
        logger.info("Завдання 2: усі JSON-файли валідні.")
    else:
        logger.info(f"Завдання 2: невалідних JSON — {invalid}. Деталі у json-лозі.")


def get_incoming_by_group_number_from_github(group_number: str):
    url = f"{BASE_URL}/work_with_xml/groups.xml"
    r = requests.get(url)
    r.raise_for_status()
    root = ET.fromstring(r.text)

    for group in root.findall(".//group"):
        number_el = group.find("number")
        if number_el is not None and (number_el.text or "").strip() == str(group_number):
            incoming_el = group.find("./timingExbytes/incoming")
            return (incoming_el.text or "").strip() if incoming_el is not None else None
    return None


def task_xml_from_github(group_number: str, logger: logging.Logger):
    try:
        val = get_incoming_by_group_number_from_github(group_number)
        if val:
            logger.info(f"Завдання 3: group/number={group_number} -> timingExbytes/incoming = {val}")
        else:
            logger.info(f"Завдання 3: для group/number={group_number} значення timingExbytes/incoming не знайдено.")
    except Exception as e:
        logger.info(f"Завдання 3: помилка при читанні XML: {e}")


def main():
    parser = argparse.ArgumentParser(description="CSV/JSON/XML tasks з GitHub (ideas_for_test).")
    parser.add_argument("--last-name", default="Melnyk",
                        help="Прізвище для назв файлів (result_<last_name>.csv, json__<last_name>.log)")
    args = parser.parse_args()

    logger = setup_logger(args.last_name)
    task_csv_from_github(args.last_name, logger)
    task_json_from_github(logger)
    task_xml_from_github(GROUP_NUMBER, logger)


if __name__ == "__main__":
    main()
