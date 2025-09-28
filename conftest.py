import pytest
from api.client import ScooterApiClient
from utils.generators import generate_courier_data

@pytest.fixture
def courier_data():
    api_client = ScooterApiClient()
    courier_data = generate_courier_data()
    """Фикстура для генерации данных курьера"""
    yield courier_data
    login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
    # Очистка - удаляем созданного курьера
    courier_id = login_response.json().get("id")
    if courier_id:
        api_client.delete_courier(courier_id)


@pytest.fixture
def registered_courier():

    api_client = ScooterApiClient()

    """Фикстура для создания и удаления тестового курьера"""
    courier_data = generate_courier_data()
    
    # Создаем курьера (используем правильные имена параметров)
    create_response = api_client.create_courier(
        login=courier_data["login"],
        password=courier_data["password"], 
        first_name=courier_data["firstName"]  
    )
    courier_id = None
    
    if create_response.status_code == 201:
        # Логинимся для получения ID
        login_response = api_client.login_courier(
            courier_data["login"], 
            courier_data["password"]
        )
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
    
    yield {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "first_name": courier_data["firstName"],  
        "id": courier_id
    }
    
    # Удаляем курьера после теста
    if courier_id:
        api_client.delete_courier(courier_id)