from httpx import Response, QueryParams
from clients.http.client import HTTPClient, HTTPCClientExtensions
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.operations.schema import (
    MakeFeeOperationRequestSchema, MakeTopUpOperationRequestSchema,
    MakeCashbackOperationRequestSchema, MakeTransferOperationRequestSchema,
    MakePurchaseOperationRequestSchema, MakeBillPaymentOperationRequestSchema,
    MakeCashWithdrawalOperationRequestSchema, MakeFeeOperationResponseSchema,
    MakeTopUpOperationResponseSchema, MakeCashbackOperationResponseSchema,
    MakeTransferOperationResponseSchema, MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema, MakeCashWithdrawalOperationResponseSchema,
    GetOperationsSummaryQuerySchema, GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema, GetOperationQuerySchema, GetOperationsResponseSchema
)
from locust.env import Environment

from tools.routes import APIRoutes


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, query: GetOperationQuerySchema) -> Response:

        """
        Выполняет GET-запрос на получение информации об операции по operation_id

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(
            APIRoutes.OPERATIONS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPCClientExtensions(route=APIRoutes.OPERATIONS)
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operations-summary",
                        params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPCClientExtensions(route=f"{APIRoutes.OPERATIONS}/operations-summary")
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции по operation_id.

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operations-receipt/{operation_id}",
            extensions=HTTPCClientExtensions(route=f"{APIRoutes.OPERATIONS}/operations-receipt/{{operation_id}}")
        )

    def get_operations_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации списка операций для определенного счета.

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operations/{operation_id}",
            extensions=HTTPCClientExtensions(route=f"{APIRoutes.OPERATIONS}/operations/{{operation_id}}")
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationQuerySchema(account_id=account_id)
        response = self.get_operation_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationsResponseSchema:
        response = self.get_operations_api(operation_id)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post(" /api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api (self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api  (self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты снятия наличных денег.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Объект httpx.Response
        """
        return self.post(" /api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())


def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayHTTPClient с хуками сбора метрик.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))