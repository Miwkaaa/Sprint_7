class ApiEndpoints:
    """Класс с эндпоинтами API Яндекс Самокат"""
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
    
    # Курьеры
    COURIER_CREATE = f"{BASE_URL}/courier"
    COURIER_LOGIN = f"{BASE_URL}/courier/login"
    COURIER_DELETE = f"{BASE_URL}/courier/{{courier_id}}"
    COURIER_ORDERS_COUNT = f"{BASE_URL}/courier/{{courier_id}}/ordersCount"
    
    # Заказы
    ORDER_CREATE = f"{BASE_URL}/orders"
    ORDER_LIST = f"{BASE_URL}/orders"
    ORDER_TRACK = f"{BASE_URL}/orders/track"
    ORDER_ACCEPT = f"{BASE_URL}/orders/accept/{{order_id}}"
    ORDER_CANCEL = f"{BASE_URL}/orders/cancel"
    ORDER_FINISH = f"{BASE_URL}/orders/finish/{{order_id}}"
    
    # Утилиты
    PING = f"{BASE_URL}/ping"
    STATIONS_SEARCH = f"{BASE_URL}/stations/search"
