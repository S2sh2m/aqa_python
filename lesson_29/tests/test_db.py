import psycopg2
from lesson_29.db import (
    get_connection,
    init_db,
    insert_result,
    update_result,
    delete_result,
    get_result,
)


def test_db_connection():
    conn = get_connection()
    assert isinstance(conn, psycopg2.extensions.connection)
    conn.close()


def test_crud_operations():
    init_db()

    new_id = insert_result("new_user", 50)
    assert isinstance(new_id, int)

    row = get_result(new_id)
    assert row is not None
    assert row["username"] == "new_user"
    assert row["score"] == 50

    update_result(new_id, 150)
    updated_row = get_result(new_id)
    assert updated_row["score"] == 150

    delete_result(new_id)
    deleted_row = get_result(new_id)
    assert deleted_row is None
