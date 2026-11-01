# Diplom_2
# Diplom_2 — API-тестирование Stellar Burgers

Проект автоматизированного тестирования API сервиса Stellar Burgers.

## Используемые технологии

- Python
- Pytest
- Requests
- Allure

## Покрытые сценарии

- Регистрация пользователя
- Авторизация пользователя
- Создание заказа

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запустить все тесты:

```bash
python3 -m pytest
```

Запустить тесты с формированием результатов Allure:

```bash
python3 -m pytest --alluredir=allure-results
```

## Формирование Allure-отчёта

```bash
allure serve allure-results
```
