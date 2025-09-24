import random
import string

def generate_random_string(length=10):
    """Генерация случайной строки"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_courier_data():
    """Генерация данных для курьера"""
    return {
        "login": f"courier_{generate_random_string(8)}",
        "password": generate_random_string(10),
        "firstName": f"Courier_{generate_random_string(6)}"
    }

def generate_order_data(color=None):
    """Генерация данных для заказа"""
    order = {
        "firstName": "Алексей",
        "lastName": "Петров",
        "address": "ул. Примерная, д. 10",
        "metroStation": "4",
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2024-12-31",
        "comment": "Тестовый заказ"
    }
    if color:
        order["color"] = color
    return order
