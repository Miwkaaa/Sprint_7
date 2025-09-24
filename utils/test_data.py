# Тестовые данные для негативных тестов
INVALID_COURIER_DATA = {
    "missing_login": {"password": "password123", "first_name": "Тест"},
    "missing_password": {"login": "test_user", "first_name": "Тест"},
     "missing_first_name": {"login": "test_user", "password": "password123"},
    "nonexistent_user": {"login": "nonexistent_user", "password": "wrong_password"}
}

ORDER_COLORS = [
    {"color": ["BLACK"], "description": "черный цвет"},
    {"color": ["GREY"], "description": "серый цвет"},
    {"color": ["BLACK", "GREY"], "description": "оба цвета"},
    {"color": [], "description": "без цвета"}
]
