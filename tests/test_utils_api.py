import allure
from api.client import ScooterApiClient

@allure.feature("API Утилиты")
class TestUtilsAPI:
    
    @allure.title("Проверка доступности сервера")
    def test_ping_server(self):
        api_client = ScooterApiClient()
        with allure.step("Отправить ping запрос"):
            response = api_client.ping_server()
            
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.text.strip().rstrip(';') == "pong"
