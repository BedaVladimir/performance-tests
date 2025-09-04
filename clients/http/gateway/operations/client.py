from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from typing import TypedDict


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения операции счета.
    """
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики операций для определенного счета.
    """
    accountId: str

class MakeFeeOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeBillPaymentOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationQueryDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции по operation_id.

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operations-receipt/{operation_id}")

    def get_operations_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post(" /api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api (self, request: MakeBillPaymentOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api  (self, request: MakeCashWithdrawalOperationQueryDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты снятия наличных денег.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post(" /api/v1/operations/make-cash-withdrawal-operation", json=request)