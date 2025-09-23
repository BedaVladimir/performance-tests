from locust import User, between, task

from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from pydantic_create_user import CreateUserResponseSchema


class OpenDebitCardAccount(User): # Наследуемся от User вместо HttpUser
    # Обязательное поле, требуемое Locust. Будет проигнорировано, но его нужно указать, иначе будет ошибка запуска.
    host = "localhost"
    wait_time = between(1, 3)

    # Поле, в котором будет храниться экземпляр нашего API клиента
    users_gateway_client: UsersGatewayHTTPClient
    # Поле, куда мы сохраним ответ после создания пользователя
    create_user_response: CreateUserResponseSchema
    # Поле, в котором будет храниться экземпляр нашего API клиента
    accounts_gateway_client: AccountsGatewayHTTPClient

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        # Шаг 1: создаем API клиент, встроенный в экосистему Locust (с хуками и поддержкой сбора метрик)
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)

        # Шаг 1: создаем API клиент, встроенный в экосистему Locust (с хуками и поддержкой сбора метрик)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

        # Шаг 2: создаем пользователя через API
        self.create_user_response = self.users_gateway_client.create_user()


    @task
    def make_debit_card_account(self):
        """
        Тест создания дебетового счета
        """
        open_debit_card_account_request = self.create_user_response.user.id
        self.accounts_gateway_client.open_debit_card_account(open_debit_card_account_request)