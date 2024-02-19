import sqlite3


def get_balance(user_id, cursor):
    """
    Функция для получения баланса пользователя.
    :param user_id: id пользователя
    :param cursor: подключение к бд
    :return: int баланс
    """
    cursor.execute("SELECT balance FROM users  WHERE id = ?", (user_id,))
    balance = cursor.fetchone()
    return balance[0] if balance else None


class User:
    def __init__(self, id, username, balance):
        """
        Инициализвция пользователя.
        :param id: id пользователя
        :param username: имя пользователя
        :param balance: баланс пользователя
        """
        self.id = id
        self.username = username
        self.balance = balance

    @staticmethod
    def create_table():
        """
        Функция для создания таблицы пользователей пользователя.
        """
        # Проверяем наличие таблицы
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            balance INTEGER NOT NULL CHECK (balance >= 0)
                        )''')
        conn.commit()
        conn.close()

    @staticmethod
    def add_user(username, balance):
        """
        Функция для создания пользователя.
        :param username: имя пользователя
        :param balance:  баланс пользователя
        """
        # Проверяем что баланс должен быть положителен
        if balance < 0:
            balance = 0
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, balance) VALUES (?, ?)', (username, balance))
        conn.commit()
        conn.close()

    @staticmethod
    def update_balance(user_id, amount, action):
        """
        Функция для обновления баланса.
        :param user_id: id пользователя
        :param amount: сумма обновления
        :param action: тип обновления
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        balance = get_balance(user_id, cursor)
        # Проверяем что баланс должен быть положителен
        if balance is None:
            balance = 0
        if action is None:
            if amount < 0:
                amount = 0
            cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (amount, user_id))
        elif action == 'Increase':
            if balance + amount < 0:
                cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (0, user_id))
            else:
                cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
        elif action == 'Decrease':
            if balance - amount < 0:
                cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (0, user_id))
            else:
                cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_users():
        """
        Функция для получения всех пользователей.
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def clear_all_users():
        """
        Функция для отчистки всех пользователей.
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users")
        conn.commit()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        """
        Функция для удаления пользователя.
        :param user_id: id пользователя
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_username(user_id, new_username):
        """
        Функция для обновления имени.
        :param user_id: id пользователя
        :param new_username: новое имя
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_id))
        conn.commit()
        conn.close()
