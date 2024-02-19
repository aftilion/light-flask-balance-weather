import requests

WEATHER_API_KEY = 'Your_API_KEY'


def fetch_weather(city):
    """
    Функция для получения погода для города с сайта openweathermap.
    :param city: наименование города
    :return: полученная температура/None ; сообщение об ошибке/None
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        if data.get('cod') == 200:
            temperature = data['main']['temp']
            return temperature, None
        elif data.get('cod') == 404:
            temperature = None
            message = data.get('message', '404 Error')
            return temperature, message
        else:
            error_message = 'Error while get temperature'
            return None, error_message

    except Exception as e:
        error_message = str(e)
        return None, error_message
