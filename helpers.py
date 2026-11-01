
import requests
from data import Url


def get_ingredients():
    response = requests.get(f'{Url.MAIN_URL}{Url.GET_INGREDIENTS}')
    return [ingredient["_id"] for ingredient in response.json()["data"][:2]]