import psycopg2
import allure
from lesson_29.db import (
    get_connection,
    init_db,
    insert_result,
    update_result,
    delete_result,
    get_result,
)



@allure.feature("DB Connection")
def test_db_connection():
    with allure.step("Конектимось"):
        conn = get_connection()

    with allure.step("Робе чи не робе"):
        assert isinstance(conn, psycopg2.extensions.connection)

    with allure.step("Розконектились"):
        conn.close()


@allure.feature("CRUD Operations")
def test_crud_operations():

    with allure.step("Init table"):
        init_db()

    with allure.step("New data"):
        new_id = insert_result("new_user", 50)
        assert isinstance(new_id, int)

    with allure.step("Check added data"):
        row = get_result(new_id)
        assert row is not None
        assert row["username"] == "new_user"
        assert row["score"] == 50

    with allure.step("Update data"):
        update_result(new_id, 150)

    with allure.step("Check updated data"):
        updated_row = get_result(new_id)
        assert updated_row["score"] == 150

    with allure.step("Delete data"):
        delete_result(new_id)

    with allure.step("Check deleted data"):
        deleted_row = get_result(new_id)
        assert deleted_row is None
