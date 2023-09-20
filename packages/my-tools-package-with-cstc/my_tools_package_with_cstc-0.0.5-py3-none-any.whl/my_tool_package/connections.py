from promptflow.contracts.types import Secret
from promptflow._core.tools_manager import register_connections
from promptflow._sdk.entities._connection import CustomStrongTypeConnection


class MyFirstConnection(CustomStrongTypeConnection):
    api_key: Secret
    api_base: str = "This is my first connection."


class MySecondConnection(CustomStrongTypeConnection):
    api_key: Secret
    api_base: str = "This is my second connection."


register_connections([MyFirstConnection, MySecondConnection])
