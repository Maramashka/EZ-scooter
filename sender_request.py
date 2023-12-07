import requests
import configuration
import data


# Создаём новый заказ

def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.CLIENT_BODY)


# Вытаскиваем номер заказа
def get_track():
    return create_new_order().json()["track"]


# Кладём трек в функцию получения нового заказа
def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + '?t=' + get_track())


# здесь ошибка TypeError, не знаю, как с ней быть :(

# Проверяем, что запрос на получение заказа успешен
def test_success_get_order():
    assert get_order.status_code == 200
