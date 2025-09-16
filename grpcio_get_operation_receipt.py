import grpc

# gRPC-клиенты для соответствующих сервисов
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest, OpenDebitCardAccountResponse)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest, MakeTopUpOperationResponse)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest, GetOperationReceiptResponse)
# Enum со статусами операций
from contracts.services.operations.operation_pb2 import OperationStatus
# Фейковые данные для тестов
from tools.fakers import fake

# Создаём gRPC-канал к сервисам, работающим на порту 9003
channel = grpc.insecure_channel("localhost:9003")

# Инициализируем stubs (gRPC-клиенты)
users_gateway_client = UsersGatewayServiceStub(channel)
account_gateway_client = AccountsGatewayServiceStub(channel)
operations_gateway_client = OperationsGatewayServiceStub(channel)

# 1. Создаём нового пользователя
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number(),
)
create_user_response: CreateUserResponse = users_gateway_client.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# 2. Открываем кредитный счёт на созданного пользователя
open_debit_card_account_request = OpenDebitCardAccountRequest(user_id = create_user_response.user.id)
open_debit_card_account_response: OpenDebitCardAccountResponse = account_gateway_client.OpenDebitCardAccount(
    open_debit_card_account_request)
print('Open debit card account response:', open_debit_card_account_response)

# 3. Создаём операцию пополнения счета, привязанную к счёту и карте
make_top_up_operation_request = MakeTopUpOperationRequest(
    account_id=open_debit_card_account_response.account.id,
    amount=fake.amount(),
    card_id=open_debit_card_account_response.account.cards[0].id,
    status=OperationStatus.OPERATION_STATUS_COMPLETED
)
make_top_up_operation_response: MakeTopUpOperationResponse = operations_gateway_client.MakeTopUpOperation(
    make_top_up_operation_request)
print('Make top up operation response:', make_top_up_operation_response)

# 4. Получаем чек по операции
get_operation_receipt_request = GetOperationReceiptRequest(operation_id=make_top_up_operation_response.operation.id)
get_operation_receipt_response: GetOperationReceiptResponse = operations_gateway_client.GetOperationReceipt(
    get_operation_receipt_request)
print('Get operation receipt response:', get_operation_receipt_response)