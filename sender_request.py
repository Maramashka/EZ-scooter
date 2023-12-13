import requests
import configuration
import data


# Мария Зверева, 11 когорта - финальный проект. Инженер по тестированию плюс

# Создаём новый заказ
def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.CLIENT_BODY)


# Вытаскиваем номер заказа
def get_track():
    track_number = create_new_order().json()["track"]
    return track_number



# Кладём трек в функцию получения нового заказа
def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + '?t=' + get_track())
