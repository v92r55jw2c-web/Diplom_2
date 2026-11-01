import requests
from generators import generate_user_data
from constants import EXPECTED_STATUS_CREATED, FORBIDDEN_STATUS, MSG_LOGIN_DUPLICATE, MSG_REQUIRED_FIELDS
import allure
from data import Url


class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    def test_create_user_success(self, user):

        response = user["response"]

        assert EXPECTED_STATUS_CREATED == response.status_code, (
            f'Ожидаемый статус-код: {EXPECTED_STATUS_CREATED}. '
            f'Фактический статус-код: {response.status_code}. '
        )
        assert response.json()["success"] is True, (
            f'Ожидаемый результат: в теле ответа присутствует поле "success" со значением "true". '
            f'Фактический результат: тело ответа {response.text}. '
        )

    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_user_duplicate(self, user):

        first_user_data = user['data'] 
        
        second_response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=first_user_data)
        
        actual_message = second_response.json()["message"]

        assert user["response"].status_code == EXPECTED_STATUS_CREATED
        
        assert FORBIDDEN_STATUS == second_response.status_code, (
            f'Ожидаемый статус-код: {FORBIDDEN_STATUS}. '
            f'Фактический статус-код: {second_response.status_code}. '
        )
        assert MSG_LOGIN_DUPLICATE in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу MSG_LOGIN_DUPLICATE. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )


    @allure.title('Создание пользователя без обязательного поля email')
    def test_without_email(self):

        user_data = generate_user_data()

        user_data.pop('email')

        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)
        
        actual_message = response.json()["message"]

        assert response.status_code == FORBIDDEN_STATUS, (
            f'Ожидаемый статус-код: {FORBIDDEN_STATUS}. '
            f'Фактический статус-код: {response.status_code}. '
        )
        assert MSG_REQUIRED_FIELDS in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу {MSG_REQUIRED_FIELDS}. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )

    @allure.title('Создание пользователя без обязательного поля Пароль')
    def test_without_password(self):
    
        user_data = generate_user_data()
    
        user_data.pop('password')
    
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)
            
        actual_message = response.json()["message"]
    
        assert response.status_code == FORBIDDEN_STATUS, (
            f'Ожидаемый статус-код: {FORBIDDEN_STATUS}. '
            f'Фактический статус-код: {response.status_code}. '
        )
        assert MSG_REQUIRED_FIELDS in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу {MSG_REQUIRED_FIELDS}. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )

    @allure.title('Создание пользователя без обязательного поля Пароль')
    def test_without_name(self):
        
        user_data = generate_user_data()
        
        user_data.pop('name')
        
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)
                
        actual_message = response.json()["message"]
        
        assert response.status_code == FORBIDDEN_STATUS, (
            f'Ожидаемый статус-код: {FORBIDDEN_STATUS}. '
            f'Фактический статус-код: {response.status_code}. '
        )
        assert MSG_REQUIRED_FIELDS in actual_message, (
            f'Ожидаемое сообщение в теле ответа содержит фразу {MSG_REQUIRED_FIELDS}. '
            f'Фактическое сообщение в теле ответа: {actual_message}. '
        )