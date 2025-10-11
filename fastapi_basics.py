# Импортируем основной класс FastAPI из библиотеки fastapi
import uvicorn
from fastapi import FastAPI, Query, Path, Body, APIRouter, HTTPException, Depends, status
from pydantic import BaseModel                  # BaseModel — базовый класс для моделей

# Создаем объект приложения FastAPI
# Параметр title задает название нашего приложения, которое будет отображаться в документации
app = FastAPI(title='basics')

# Настраиваем роутер с префиксом и тегом
router = APIRouter(
    prefix="/api/v1", # общий префикс для всех путей в этом роутере
    tags=["Basics"]   # в Swagger UI группа будет помечена тегом "Basics"
)

# Pydantic-модель для описания структуры пользователя
class User(BaseModel):
    username: str  # логин пользователя
    email: str     # email пользователя
    age: int       # возраст пользователя

# Модель ответа
class UserResponse(BaseModel):
    username: str
    email: str
    message: str


# Зависимость: проверка минимального возраста
def validate_min_age(min_age: int = 18):
    def checker(user: User):
        if user.age < min_age:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User must be at least {min_age} years old"
            )
        return user

    return checker

# GET /api/v1/basics/{item_id}?name=...
@router.get("/basics/{item_id}")
async def get_basics(
        name: str = Query(                 # объявляем query-параметр name
            default="Alice",               # значение по умолчанию
            description="Имя пользователя" # описание в Swagger UI
        ),
        item_id: int = Path(
            ...,                                # path-параметр item_id
            description="Идентификатор пользователя"   # обязательный (без default)
        )
):  # возвращаем персонализированное сообщение
    return {"message": f"hello {name}",
            "description": f"item number {item_id}"}


# POST-эндпоинт для создания пользователя
# response_model=UserResponse — в документации и при выводе будет только то, что описано в UserResponse
@router.post("/basics/users",
          response_model=UserResponse)
async def create_user(
    user: User = Body(..., description="Данные нового пользователя")
) -> UserResponse:
    # FastAPI автоматически:
    # 1) распарсит JSON из тела запроса
    # 2) провалидирует его по полям модели User
    return UserResponse(
        username=user.username,
        email=user.email,
        message="User created successfully!"
    )

# Эндпоинт использует Depends для валидации возраста
@router.post("/basics/register", summary="Регистрация пользователя с проверкой возраста")
async def register_user(
        user: User = Depends(validate_min_age(min_age=21))  # внедряем зависимость
):
    return {
        "message": f"User {user.username} registered successfully",
        "email": user.email,
        "age": user.age
    }


# Подключаем роутер к основному приложению
app.include_router(router)


# --------------------------------------------------------
# Программный запуск приложения
# --------------------------------------------------------
if __name__ == "__main__":
    # Запускаем Uvicorn с указанием:
    # - имя модуля и объекта приложения (fastapi_basics:app)
    # - адрес и порт (host, port)
    # - авто-перезагрузка при изменении кода (reload=True)
    uvicorn.run(
        "fastapi_basics:app",  # "<module_name>:<app_instance>"
        host="127.0.0.1",  # адрес, на котором слушаем входящие подключения
        port=9000,  # порт
        reload=True,  # перезагрузка при изменении файлов
        log_level="info"  # уровень логирования
    )