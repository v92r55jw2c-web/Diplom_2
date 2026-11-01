import pytest
import requests
from data import Url
from generators import generate_user_data
from faker import Faker

@pytest.fixture
def user():
    user_data = generate_user_data()
    response = requests.post(
        f'{Url.MAIN_URL}{Url.CREATE_USER}',
        json=user_data
    )

    yield {
        "data": user_data,
        "response": response,
        "access_token": response.json().get("accessToken")
    }

fake = Faker()

@pytest.fixture
def invalid_ingredient_hash():
    return fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^')    