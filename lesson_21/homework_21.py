import datetime

LOG_FILE = "hblog.txt"
KEY = "Key TSTFEED0300|7E3E|0400"
OUTPUT = "hb_test.log"


def parse_time(line: str) -> datetime.datetime:
    pos = line.find("Timestamp ")
    if pos == -1:
        return None

    time_str = line[pos + len("Timestamp "): pos + len("Timestamp ") + 8]
    return datetime.datetime.strptime(time_str, "%H:%M:%S")


def analyze_heartbeat():
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    filtered = [line.strip() for line in lines if KEY in line]

    timestamps = [parse_time(line) for line in filtered]
    timestamps = [t for t in timestamps if t is not None]

    with open(OUTPUT, "w") as out:
        out.write("Heartbeat log\n")

        for i in range(len(timestamps) - 1):
            t1 = timestamps[i]
            t2 = timestamps[i + 1]

            delta = abs((t1 - t2).total_seconds())

            if 31 < delta < 33:
                out.write(f"WARNING: Heartbeat {delta} sec at {t1.time()}\n")
            elif delta >= 33:
                out.write(f"ERROR: Heartbeat {delta} sec at {t1.time()}\n")



if __name__ == "__main__":
    analyze_heartbeat()
