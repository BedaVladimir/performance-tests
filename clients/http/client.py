from httpx import Client, URL, QueryParams, Response
from typing import Any, TypedDict

from wsproto import extensions


# Тип расширений, которые можно передать в запрос
class HTTPCClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    """
    Базовый HTTP API клиент, принимающий объект httpx.Client.

    :param client: экземпляр httpx.Client для выполнения HTTP-запросов
    """

    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            extensions: HTTPCClientExtensions | None = None # Добавили поддержку extensions
    ) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :param extensions: Дополнительные данные, передаваемые через HTTPX extensions.
        :return: Объект Response с данными ответа.
         """
        return self.client.get(url, params=params, extensions=extensions)

    def post(
            self,
             url: URL | str,
             json: Any | None = None,
             extensions: HTTPCClientExtensions | None = None # Добавили поддержку extensions
    ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param extensions: Дополнительные данные, передаваемые через HTTPX extensions.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, json=json, extensions=extensions)

