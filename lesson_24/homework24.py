import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("cars_test_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

@pytest.fixture(scope="class")
def auth_session():

    session = requests.Session()

    logger.info("Authenticating test_user...")
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200, "Authentication failed!"

    token = response.json()["access_token"]
    logger.info(f"Received token: {token[:20]}...")

    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 10),
        ("brand", 7),
        ("price", 15),
        ("year", None),
        (None, 5),
    ]
)
class TestSearchCars:

    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"Request with params: {params}")

        response = auth_session.get(f"{BASE_URL}/cars", params=params)

        assert response.status_code == 200, "Request to /cars failed!"

        cars = response.json()

        logger.info(f" {len(cars)} cars")

        if limit:
            assert len(cars) <= limit, f"Returned more items than limit={limit}"

        if sort_by:
            sorted_by_api = [car[sort_by] for car in cars]
            sorted_locally = sorted(sorted_by_api)
            assert sorted_by_api == sorted_locally, f"Cars are not sorted by {sort_by}"

        logger.info(f"Test passed for sort_by={sort_by}, limit={limit}\n")
