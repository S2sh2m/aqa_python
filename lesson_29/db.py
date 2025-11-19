import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "testuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "testpassword")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5439")

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        cursor_factory=RealDictCursor,
    )


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS test_results (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            score INTEGER NOT NULL
        );
        """
    )
    conn.commit()
    cur.close()
    conn.close()


def insert_result(username: str, score: int) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO test_results (username, score) VALUES (%s, %s) RETURNING id;",
        (username, score),
    )
    new_id = cur.fetchone()["id"]
    conn.commit()
    cur.close()
    conn.close()
    return new_id


def update_result(result_id: int, new_score: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE test_results SET score = %s WHERE id = %s;",
        (new_score, result_id),
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_result(result_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM test_results WHERE id = %s;", (result_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_result(result_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_results WHERE id = %s;", (result_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row
