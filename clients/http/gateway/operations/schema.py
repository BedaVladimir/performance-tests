from enum import StrEnum
from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from tools.fakers import fake


class OperationType(StrEnum):
    """
    Enum с типами операций
    """
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры операции для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias='cashbackAmount')


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры операции для получения чека
    """
    url: HttpUrl
    document: str


class GetOperationQuerySchema(BaseModel):
    """
    Структура данных для получения операции счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Структура данных ответа списка операций для определенного счета.
    """
    operations: OperationSchema


class GetOperationResponseSchema(BaseModel):
    """
    Структура данных ответа получение информации об операции.
    """
    operation: OperationSchema


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура данных ответа операции для получения статистики по операциям для определенного счета.
    """
    summary:OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура данных ответа операции для получения чека.
    """
    receipt: OperationReceiptSchema


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: str = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeOperationResponseSchema(BaseModel):
    """
    Базовая описание структуры тела ответа для создания финансовой операции
    """
    operation: OperationSchema


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeFeeOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeTopUpOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeCashbackOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakeTransferOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции покупки.
    """
    pass


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeBillPaymentOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции оплаты по счету.
    """
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа создания операции снятия наличных денег.
    """
    pass