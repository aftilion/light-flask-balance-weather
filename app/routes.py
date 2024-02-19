# routes.py

from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app.models.user import User
from app.weather import fetch_weather


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Эндпоинт для рендеринга базовой страницы.
    :return: index.html базовый эндпоинт
    """
    if request.method == 'POST':
        username = request.form['username']
        balance = int(request.form['balance'])
        User.add_user(username, balance)
        return redirect(url_for('index'))
    users = User.get_all_users()
    return render_template('index.html', users=users)


@app.route('/update_balance', methods=['POST'])
def update_balance():
    """
    Эндпоинт для обновления баланса пользователя.
    :return: index.html базовый эндпоинт
    """
    user_id = request.form['user_id']
    amount = int(request.form['amount'])
    action = request.form.get('action_balance', None)
    if action != 'Decrease' or action != 'Increase' or action is not None:
        action = None
    User.update_balance(user_id, amount, action)
    return redirect(url_for('index'))


@app.route('/update_username', methods=['POST'])
def update_username():
    """
    Эндпоинт для обновления имени пользователя.
    :return: index.html базовый эндпоинт
    """
    user_id = request.form['user_id']
    new_username = request.form['username']
    User.update_username(user_id, new_username)
    return redirect(url_for('index'))


@app.route('/delete_user', methods=['POST'])
def delete_user():
    """
    Эндпоинт для удаления пользователя.
    :return: index.html базовый эндпоинт
    """
    user_id = request.form['user_id']
    User.delete_user(user_id)
    return redirect(url_for('index'))


@app.route('/update_balance_by_city', methods=['POST'])
def update_balance_by_city():
    """
    Эндпоинт для обновления баланса пользователя используя город.
    :return: index.html базовый эндпоинт
    """
    user_id = request.form.get('user_id')
    city = request.form.get('city')
    action = request.form.get('action_balance', None)
    if action != 'Decrease' and action != 'Increase' and action is not None:
        action = None
    temperature, error = fetch_weather(city)
    if error:
        return redirect(url_for('index', error=error))
    User.update_balance(user_id, temperature, action)
    return redirect(url_for('index'))


