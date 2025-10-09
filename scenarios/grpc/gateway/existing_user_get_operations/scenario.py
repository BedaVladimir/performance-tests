from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_get_documents import ExistingUserGetDocumentsSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


# Этот хук выполняется один раз при инициализации теста (до старта пользователей).
# Мы используем его, чтобы заранее прогнать сидинг и загрузить пользователей в память.
@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Создаем экземпляр сидинг-сценария
    seeds_scenario = ExistingUserGetDocumentsSeedsScenario()

    # Выполняем генерацию данных, если они ещё не созданы
    seeds_scenario.build()

    # Загружаем сгенерированных пользователей в окружение Locust
    environment.seeds = seeds_scenario.load()


# Набор задач (TaskSet), который будет выполняться виртуальными пользователями.
class GetDocumentsTaskSet(GatewayGRPCTaskSet):
    # Типизируем объект пользователя из сидинга
    seed_user: SeedUserResult

    # Метод вызывается при запуске каждой сессии пользователя (до начала задач)
    def on_start(self) -> None:
        super().on_start()

        # Получаем следующего пользователя из списка (по порядку!)
        self.seed_user = self.user.environment.seeds.get_next_user()

    @task(1)
    def get_accounts(self):
        # Запрашиваем список счетов
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(2)
    def get_operations(self):
        # Запрашиваем список операций для счета
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_operations_summary(self):
        # Получаем статистику операций по определенному счету
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    # Конкретный пользовательский класс, у которого в качестве задач используется GetDocumentsTaskSet


class GetDocumentsScenarioUser(LocustBaseUser):
    tasks = [GetDocumentsTaskSet]