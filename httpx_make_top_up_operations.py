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

# Выводим полученные данные пользователя
print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)

open_debit_card_account_payload = {
  "userId": create_user_response_data['user']['id']
}

# Выполнение запроса на создание дебетового счета
open_debit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account",
                                              json = open_debit_card_account_payload)
open_debit_card_account_response_data = open_debit_card_account_response.json()
print("Open Debit Card Account response:", open_debit_card_account_response_data)

# Данные для пополнения дебетовой карты
make_top_up_operations_payload = {
  "status": "COMPLETED",
  "amount": 1500,
  "cardId": open_debit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_debit_card_account_response_data['account']['id']
}

# Выполнение запроса на пополнение карты
make_top_up_operations_response = httpx.post("http://localhost:8003/api/v1/operations/make-top-up-operation",
                                             json=make_top_up_operations_payload)
make_top_up_operations_response_data = make_top_up_operations_response.json()
print("Make top up operations response:", make_top_up_operations_response_data)
print("Status Code:", make_top_up_operations_response.status_code)
