import sender_request


# Проверяем, что запрос на получение заказа успешен
def test_success_get_order():
    new_order = sender_request.get_order()
    assert new_order.status_code == 200
