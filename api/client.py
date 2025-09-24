import requests
from .endpoints import ApiEndpoints

class ScooterApiClient:
    """Клиент для работы с API Яндекс Самокат"""
    
    def __init__(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1"
    
    def create_courier(self, login, password, first_name):
        """Создание нового курьера"""
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name  
        }
        return requests.post(ApiEndpoints.COURIER_CREATE, json=payload)
    
    def login_courier(self, login, password):
        """Логин курьера"""
        payload = {"login": login, "password": password}
        return requests.post(ApiEndpoints.COURIER_LOGIN, json=payload)
    
    def delete_courier(self, courier_id):
        """Удаление курьера"""
        return requests.delete(ApiEndpoints.COURIER_DELETE.format(courier_id=courier_id))
    
    def create_order(self, order_data):
        """Создание заказа"""
        return requests.post(ApiEndpoints.ORDER_CREATE, json=order_data)
    
    def get_orders_list(self, params=None):
        """Получение списка заказов"""
        return requests.get(ApiEndpoints.ORDER_LIST, params=params)
    
    def ping_server(self):
        """Проверка доступности сервера"""
        response = requests.get(ApiEndpoints.PING)
        if response.text.endswith(';'):
            response._content = response.content.replace(b';', b'')
        return response