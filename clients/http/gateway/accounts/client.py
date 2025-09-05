from httpx import Response
from clients.http.client import HTTPClient, QueryParams
from typing import TypedDict
from clients.http.gateway.client import build_gateway_http_client


class GetAccountQueryDict(TypedDict):
    """
    Структура данных для получения списка счетов пользователя.
    """
    userId: str

class OpenDepositAccountRequestDict(TypedDict):
    """
    Структура данных для открытия депозитного счета.
    """
    userId: str

class OpenSavingsAccountRequestDict(TypedDict):
    """
    Структура данных для открытия сберегательного счета.
    """
    userId: str

class OpenDebitCardAccountRequestDict(TypedDict):
    """
    Структура данных для открытия дебетового счета.
    """
    userId: str

class OpenCreditCardAccountRequestDict(TypedDict):
    """
    Структура данных для открытия кредитного счета.
    """
    userId: str

class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """

    def get_accounts_api(self, query: GetAccountQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(f"/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Функция создаёт экземпляр AccountsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())