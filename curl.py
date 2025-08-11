# Получить всех продавцов
curl -X GET "http://127.0.0.1:8000/sellers/"

# Получить продавца по ID
curl -X GET "http://127.0.0.1:8000/sellers/1/"

# Обновить продавца
curl -X PUT "http://127.0.0.1:8000/sellers/1/update/" \
-H "Content-Type: application/json" \
-d '{"name": "Иван Иванов", "email": "ivan@example.com", "phone": "+79161234567"}'