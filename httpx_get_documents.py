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

# Данные для создания счета
open_credit_card_account_payload = {
  "userId": create_user_response_data['user']['id']
}

# Выполнение запроса на создание дебетового счета
open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                              json = open_credit_card_account_payload)
open_debit_card_account_response_data = open_credit_card_account_response.json()
print("Open Debit Card Account response:", open_debit_card_account_response_data)

get_tariff_document = httpx.get(f"http://localhost:8003/api/v1/documents/tariff-document/"
          f"{open_debit_card_account_response_data['account']['id']}")
get_tariff_document_response = get_tariff_document.json()
print("Get Tariff Document response:", get_tariff_document_response)
print("Status Code:", get_tariff_document.status_code)