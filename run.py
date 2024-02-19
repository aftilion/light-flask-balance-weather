# run.py

from app import app
from app.models.user import User

if __name__ == '__main__':
    # Очищаем список всех пользователей
    User.clear_all_users()

    # Создаем новых пользователей
    users = [
        ('Alex', 10000),
        ('John', 7500),
        ('Emily', 6000),
        ('Michael', -8000),
        ('Sophia', 12000)
    ]
    for username, balance in users:
        User.add_user(username, balance)

    app.run(debug=True, port=8000)
