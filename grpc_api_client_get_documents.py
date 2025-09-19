from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.documents.client import build_documents_gateway_grpc_client
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client

user_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
documents_gateway_users = build_documents_gateway_grpc_client()

# Создаем пользователя
create_user_response = user_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открываем кредитный счет
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(create_user_response.user.id)
print('Create credit card account response:', open_credit_card_account_response)

# Сохраняем account_id, чтобы чуть сократить длину строк получения документов тарифа и контракта
account_id = open_credit_card_account_response.account.id

# Получаем документ тарифа
get_tariff_document_response = documents_gateway_users.get_tariff_document(account_id)
print('Get tariff document response:', get_tariff_document_response)

# Получаем документ контракта
get_contract_document_response = documents_gateway_users.get_contract_document(account_id)
print('Get contract document response:', get_contract_document_response)