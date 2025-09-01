import httpx # Импортируем библиотеку HTTPX
import time


# тело запроса для создания пользователя
create_user_payload_data = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

# Выполнение запроса на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload_data)
create_user_response_data = create_user_response.json()

# Вывод полученных данных и проверка статус кода
print("Create user response:", create_user_response_data)
assert create_user_response.status_code == 200, "Пользователь не создан"

# Сохранение в переменную айди пользователя
get_user_id_response = create_user_response_data['user']['id']
print(get_user_id_response)

# тело запроса с айди пользователя для создания депозитного счета
create_deposit_account_payload_data = {
  "userId": get_user_id_response
}

# Выполнение запроса на создание депозитного счета
create_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",
                                             json=create_deposit_account_payload_data)
create_deposit_account_response_data = create_deposit_account_response.json()

# Вывод полученных данных и проверка статус кода
print("Create deposit account response:", create_deposit_account_response_data)
assert create_deposit_account_response.status_code == 200, "Счет не создан"



