import requests
from data import Url
from constants import EXPECTED_STATUS_SUCCESS, MSG_UNAUTHORIZED, EXPECTED_STATUS_UNAUTHORIZED
import allure

class TestLoginUser:

    @allure.title('Успешная авторизация пользователя')
    def test_login_success(self, user):

        email = user['data']['email']
        password = user['data']['password']
        
        response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json={'email': email, 'password': password})
        
        assert EXPECTED_STATUS_SUCCESS == response.status_code, (
            f'Ожидаемый статус-код: 200. '
            f'Фактический статус-код: {response.status_code}. '
        )

        assert 'accessToken' in response.json(), (
            f'Ожидаемый результат: в теле ответа присутствует поле "accssesToken". '
            f'Фактический результат: тело ответа {response.text}. '
        )



    @allure.title('Авторизация пользователя с неправильным паролем')
    def test_login_incorrect_password(self, user):

        email = user['data']['email']

        response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json={'email': email, 'password': '12345'})
        actual_message = response.json()["message"]
        
        assert EXPECTED_STATUS_UNAUTHORIZED == response.status_code, (
            f'Ожидаемый статус-код: 401. '
            f'Фактический статус-код: {response.status_code}. '
            f'Тело ответа: {response.text}'
        )

        assert MSG_UNAUTHORIZED in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу {MSG_UNAUTHORIZED}. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )


    @allure.title('Авторизация пользователя с неправильным email')
    def test_login_incorrect_password(self, user):

        password = user['data']['password']

        response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json={'email': 'uncorrect@yandex.ru', 'password': 'password'})
        actual_message = response.json()["message"]
        
        assert EXPECTED_STATUS_UNAUTHORIZED == response.status_code, (
            f'Ожидаемый статус-код: 401. '
            f'Фактический статус-код: {response.status_code}. '
            f'Тело ответа: {response.text}'
        )

        assert MSG_UNAUTHORIZED in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу {MSG_UNAUTHORIZED}. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )