﻿
# Яндекс.Прилавок. Автотесты

Автотест на проверку эндпоинта POST /api/v1/orders на создание заказа
и эндпоинта GET /api/v1/orders/track на получение заказа.

Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.

- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
- Один тест - одна проверка
