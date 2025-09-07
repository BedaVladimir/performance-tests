from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from typing import TypedDict
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры операции для получения статистики по операциям для определенного счета.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class OperationReceiptDict(TypedDict):
    """
    Описание структуры операции для получения чека
    """
    url: str
    document: str


class GetOperationQueryDict(TypedDict):
    """
    Структура данных для получения операции счета.
    """
    accountId: str


class GetOperationsResponseDict(TypedDict):
    """
    Структура данных ответа списка операций для определенного счета.
    """
    operations: OperationDict


class GetOperationResponseDict(TypedDict):
    """
    Структура данных ответа получение информации об операции.
    """
    operation: OperationDict


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики операций для определенного счета.
    """
    accountId: str


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура данных ответа операции для получения статистики по операциям для определенного счета.
    """
    summary:OperationsSummaryDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура данных ответа операции для получения чека.
    """
    receipt: OperationReceiptDict


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeOperationResponseDict(TypedDict):
    """
    Базовая описание структуры тела ответа для создания финансовой операции
    """
    operations: OperationDict


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeFeeOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeTopUpOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeCashbackOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakeTransferOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakePurchaseOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции покупки.
    """
    pass


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeBillPaymentOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции оплаты по счету.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    pass


class MakeCashWithdrawalOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа создания операции снятия наличных денег.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, query: GetOperationQueryDict) -> Response:

        """
        Выполняет GET-запрос на получение информации об операции по operation_id

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
        Выполняет GET-запрос на получение информации списка операций для определенного счета.

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operations/{operation_id}")

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationQueryDict(accountId=account_id)
        response = self.get_operation_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationsResponseDict:
        response = self.get_operations_api(operation_id)
        return response.json()

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post(" /api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api (self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api  (self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты снятия наличных денег.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post(" /api/v1/operations/make-cash-withdrawal-operation", json=request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=100,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=200,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=300,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=400,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=500,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=600,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=700,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())