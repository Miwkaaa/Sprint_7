import pytest
import allure
from utils.generators import generate_order_data
from utils.test_data import ORDER_COLORS

@allure.feature("API Заказы")
class TestOrdersAPI:
    
    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize("color_data", ORDER_COLORS)
    def test_create_order_with_colors(self, color_data, api_client):
        with allure.step("Подготовить данные заказа"):
            order_data = generate_order_data(color_data["color"])
            
        with allure.step("Создать заказ"):
            response = api_client.create_order(order_data)
            
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            result = response.json()
            assert "track" in result
            assert isinstance(result["track"], int)
    
    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self, api_client):
        with allure.step("Создать заказ без цвета"):
            order_data = generate_order_data()
            response = api_client.create_order(order_data)
            
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert "track" in response.json()
    
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self, api_client):
        with allure.step("Запросить список заказов"):
            response = api_client.get_orders_list()
            
        with allure.step("Проверить структуру ответа"):
            assert response.status_code == 200
            result = response.json()
            assert "orders" in result
            assert isinstance(result["orders"], list)
            assert "pageInfo" in result
    
    @allure.title("Получение заказов с лимитом")
    def test_get_orders_with_limit(self, api_client):
        with allure.step("Запросить заказы с лимитом 5"):
            response = api_client.get_orders_list({"limit": 5})
            
        with allure.step("Проверить ограничение количества"):
            assert response.status_code == 200
            orders = response.json()["orders"]
            assert len(orders) <= 5
