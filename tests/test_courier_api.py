import pytest
import allure
from api.client import ScooterApiClient
from utils.generators import generate_courier_data
from utils.test_data import INVALID_COURIER_DATA

@allure.feature("API Курьеры")
class TestCourierAPI:
    
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data):
        api_client = ScooterApiClient()
        with allure.step("Создать нового курьера"):
            response = api_client.create_courier(
                login=courier_data["login"],
                password=courier_data["password"],
                first_name=courier_data["firstName"]
            )
            
        with allure.step("Проверить что курьер создан"):
            assert response.status_code == 201
            assert "ok" in response.json()
            
        with allure.step("Убедиться что можно авторизоваться под созданным курьером"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            assert login_response.status_code == 200
            assert "id" in login_response.json()
    
    @allure.title("Создание курьера с дублирующимся логином")
    def test_create_duplicate_courier(self, registered_courier):
        api_client = ScooterApiClient()
        with allure.step("Попытка создать курьера с существующим логином"):
            duplicate_data = generate_courier_data()
            duplicate_data["login"] = registered_courier["login"]
            
            response = api_client.create_courier(
                login=duplicate_data["login"],
                password=duplicate_data["password"],
                first_name=duplicate_data["firstName"]
            )
            
        with allure.step("Проверить ошибку конфликта"):
            assert response.status_code == 409
            assert "message" in response.json()
    
    @allure.title("Создание курьера без обязательных полей")
    @pytest.mark.parametrize("field, expected_code", [
        ("missing_login", 400),
        ("missing_password", 400),
        ("missing_first_name", 400)
    ])
    def test_create_courier_missing_fields(self, field, expected_code):
        api_client = ScooterApiClient()
        with allure.step(f"Создание курьера без поля {field}"):
            payload = INVALID_COURIER_DATA[field]
            # Передаем параметры явно с правильными именами
            login = payload.get("login")
            password = payload.get("password")
            first_name = payload.get("first_name")
            
            response = api_client.create_courier(
                login=login,
                password=password,
                first_name=first_name
            )
            
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == expected_code
            assert "message" in response.json()
    
    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, registered_courier):
        api_client = ScooterApiClient()
        with allure.step("Логин с валидными данными"):
            response = api_client.login_courier(
                registered_courier["login"],
                registered_courier["password"]
            )
            
        with allure.step("Проверить успешный логин"):
            assert response.status_code == 200
            assert "id" in response.json()
    
    @allure.title("Логин с неверным паролем")
    def test_login_wrong_password(self, registered_courier):
        api_client = ScooterApiClient()
        with allure.step("Логин с неверным паролем"):
            response = api_client.login_courier(
                registered_courier["login"],
                "wrong_password"
            )
            
        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 404
            assert "message" in response.json()
    
    @allure.title("Логин несуществующего пользователя")
    def test_login_nonexistent_user(self):
        api_client = ScooterApiClient()
        with allure.step("Логин с несуществующими данными"):
            payload = INVALID_COURIER_DATA["nonexistent_user"]
            response = api_client.login_courier(
                login=payload["login"],
                password=payload["password"]
            )
            
        with allure.step("Проверить ошибку не найден"):
            assert response.status_code == 404
            assert "message" in response.json()