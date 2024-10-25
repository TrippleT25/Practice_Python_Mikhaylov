import sqlite3


def get_most_values(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = [col[1] for col in cursor.fetchall()]

    result = {}

    for col in columns:
        cursor.execute(f"""
        SELECT {col}, COUNT({col}) as cnt 
        FROM {table_name}
        GROUP BY {col} 
        ORDER BY cnt DESC
        LIMIT 1;
        """)

        most_value = cursor.fetchone()
        if most_value:
            result[col] = {
                'most_value': most_value[0],
                'most_value_count': most_value[1]
            }

    conn.close()
    return result

db_name = "DATABase.db"
table_name = "users"
print(get_most_values(db_name, table_name))
