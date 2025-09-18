from grpc import Channel

from clients.grpc.client import GRPCClient
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет высокоуровневые методы для работы с операциями.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с данными операции.
        """
        return self.stub.GetOperation(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос с ID аккаунта.
        :return: Ответ от сервиса со списком операций для данного счета.
        """
        return self.stub.GetOperations(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с чеком по операции.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос с ID аккаунта.
        :return: Ответ от сервиса со статистикой операций по определенному счету.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос с данными операции комиссии.
        :return: Ответ от сервиса с операцией комиссии.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос с данными операции пополнения.
        :return: Ответ от сервиса с операцией пополнения.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос с данными операции кэшбэка.
        :return: Ответ от сервиса с операцией кэшбэка.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос с данными операции покупки.
        :return: Ответ от сервиса с операцией покупки.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос с данными операции перевода.
        :return: Ответ от сервиса с операцией перевода.
        """
        return self.stub.MakeTransferOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> (
            MakeBillPaymentOperationResponse):
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос с данными операции оплаты по счету.
        :return: Ответ от сервиса с операцией оплаты по счету.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> (
            MakeCashWithdrawalOperationResponse):
        """
        Низкоуровневый вызов метода MakeCashWithdrawalPaymentOperation через gRPC.

        :param request: gRPC-запрос с данными операции снятия наличных денег.
        :return: Ответ от сервиса с операцией снятия наличных денег.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponse:
        request = MakeFeeOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponse:
        request = MakeTopUpOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponse:
        request = MakeCashbackOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cashback_operation_api(request)

    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponse:
        request = MakePurchaseOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            category=fake.category(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_purchase_operation_api(request)

    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponse:
        request = MakeTransferOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_transfer_operation_api(request)

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponse:
        request = MakeBillPaymentOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, account_id: str, card_id: str) -> MakeCashWithdrawalOperationResponse:
        request = MakeCashWithdrawalOperationRequest(
            account_id=account_id,
            amount=fake.amount(),
            card_id=card_id,
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cash_withdrawal_operation_api(request)