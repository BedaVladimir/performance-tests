import time
import httpx  # Импортируем библиотеку HTTPX

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Проверка, что запрос по созданию клиента успешно выполнен
assert create_user_response.status_code == 200, "Клиент не создан"

# Данные для открытия кредитного счета
open_credit_card_account_payload = {
  "userId": create_user_response_data['user']['id']
}

# Выполнение запроса на создание дебетового счета
open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                              json = open_credit_card_account_payload)
open_credit_card_account_response_data = open_credit_card_account_response.json()

# Проверка, что запрос по созданию кредитного счета успешно выполнен
assert open_credit_card_account_response.status_code == 200, "Счет не создан"

# Данные для совершения операции покупки
purchase_operations_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_credit_card_account_response_data['account']['id'],
  "category": "taxi"
}

# Выполнение запроса на совершение покупки
make_top_up_operations_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                             json=purchase_operations_payload)
make_top_up_operations_response_data = make_top_up_operations_response.json()

# Проверка, что запрос по совершению покупки выполнен
assert make_top_up_operations_response.status_code == 200

# Выполнение запроса по поиску операции
get_operation_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/"
                                           f"{make_top_up_operations_response_data['operation']['id']}")

# Вывести ответ и проверить статус код
print(get_operation_receipt_response.json())
assert get_operation_receipt_response.status_code == 200, "Не удалось найти чек по данному айди операции"

