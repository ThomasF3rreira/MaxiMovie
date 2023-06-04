import sqlite3


def create_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT,
            annee INTEGER,
            acteurs TEXT,
            realisation TEXT,
            producteur TEXT,
            image TEXT
        )
    ''')

    conn.close()


create_db()
