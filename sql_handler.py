import sqlite3

DB_PATH = "ecommerce.db"

def execute_sql_query(query: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in result]
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()

def get_db_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    schema = ""
    for table_name in tables:
        table = table_name[0]
        cursor.execute(f"PRAGMA table_info({table});")
        cols = cursor.fetchall()
        schema += f"\nTable: {table}\n"
        for col in cols:
            schema += f"  {col[1]} ({col[2]})\n"
    conn.close()
    return schema
