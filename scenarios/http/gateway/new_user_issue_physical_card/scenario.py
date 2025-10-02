from locust import task

from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from clients.http.gateway.cards.schema import IssueVirtualCardResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from pydantic_create_user import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


# Класс сценария: описывает последовательный флоу нового пользователя
class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    # Храним ответы от предыдущих шагов, чтобы использовать их в следующих задачах
    create_user_response: CreateUserResponseSchema | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None
    issue_virtual_card_response: IssueVirtualCardResponseSchema | None = None

    @task
    def create_user(self):
        # Первый шаг — создать нового пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_open_debit_card_account(self):
        # Невозможно открыть счёт без созданного пользователя
        if not self.create_user_response:
            return
        # Открываем дебетовый счёт для нового пользователя
        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def issue_virtual_card(self):
        # Невозможно создать карту без созданного счета
        if not self.open_debit_card_account_response:
            return
        # Создаем виртуальную карту для нового пользователя
        self.issue_virtual_card_response = self.cards_gateway_client.issue_virtual_card(
            user_id=self.create_user_response.user.id,
            account_id=self.open_debit_card_account_response.account.id
        )


# Класс пользователя — связывает TaskSet со средой исполнения Locust
class IssuePhysicalCardSequentialTaskSetScenarioUser(LocustBaseUser):
    # Назначаем сценарий, который будет выполняться этим пользователем
    tasks = [IssuePhysicalCardSequentialTaskSet]