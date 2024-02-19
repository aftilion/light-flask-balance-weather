import sqlite3


def create_database():
    """
    Функция для создания таблицы пользователей пользователя.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        balance INTEGER NOT NULL CHECK (balance >= 0)
                    )''')
    conn.commit()
    conn.close()
