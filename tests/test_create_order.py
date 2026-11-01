import requests
import allure
from constants import EXPECTED_STATUS_BAD_REQUEST, EXPECTED_STATUS_UNAUTHORIZED, MSG_WITHOUT_INREDIENT, EXPECTED_STATUS_SUCCESS, EXPECTED_STATUS_INVALID_INREDIENT
from data import Url
from helpers import get_ingredients

class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization(self, user):
        ingredients = get_ingredients()

        order_data = {
            "ingredients": ingredients
        }

        headers = {
            "Authorization": user["access_token"]
        }

        response = requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_ORDER}',
            json=order_data,
            headers=headers
        )

        assert response.status_code == EXPECTED_STATUS_SUCCESS, (
            f'Ожидаемый статус-код: {EXPECTED_STATUS_SUCCESS}. '
            f'Фактический статус-код: {response.status_code}. '
        )

        assert response.json()["success"] is True
        assert "number" in response.json()["order"]


    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self):
        ingredients = get_ingredients()
    
        order_data = {
            "ingredients": ingredients
        }
    
        response = requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_ORDER}',
            json=order_data
        )
        
        assert EXPECTED_STATUS_UNAUTHORIZED == response.status_code, (
            f'Ожидаемый статус-код: {EXPECTED_STATUS_UNAUTHORIZED}. '
            f'Фактический статус-код: {response.status_code}. '
        )



    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, user):

        order_data = {
            "ingredients": []
        }

        headers = {
            "Authorization": user["access_token"]
        }

        response = requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_ORDER}',
            json=order_data,
            headers=headers
        )

        actual_message = response.json().get("message", "")

        assert response.status_code == EXPECTED_STATUS_BAD_REQUEST, (
            f'Ожидаемый статус-код: {EXPECTED_STATUS_BAD_REQUEST}. '
            f'Фактический статус-код: {response.status_code}. '
        )
        assert response.json()["success"] is False

        assert MSG_WITHOUT_INREDIENT in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу {MSG_WITHOUT_INREDIENT}. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )  



@allure.title('Создание заказа с некорректным хешем ингредиента')
def test_create_order_with_invalid_ingredient(user, invalid_ingredient_hash):
    order_data = {
        "ingredients": [invalid_ingredient_hash]
    }

    headers = {"Authorization": user["access_token"]}

    response = requests.post(
        f'{Url.MAIN_URL}{Url.CREATE_ORDER}',
        json=order_data,
        headers=headers
    )

    assert response.status_code == EXPECTED_STATUS_INVALID_INREDIENT, (
        f'Ожидаемый статус-код: {EXPECTED_STATUS_INVALID_INREDIENT}. '
        f'Фактический статус-код: {response.status_code}.'
    )