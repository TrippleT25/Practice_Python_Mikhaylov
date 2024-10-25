import sqlite3

def create_data_basa():
    conn = sqlite3.connect('DATABase.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    );
    ''')

    cursor.execute("INSERT INTO users (name, age) VALUES ('Николай', 30);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Андрей', 20);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Владимир', 24);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Александр', 24);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Николай', 24);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Андрей', 25);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Никита', 24);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Андрей', 29);")

    conn.commit()
    conn.close()

    print("Содержимое базы создано")

create_data_basa()
