from .auth import Auth
import aws_cdk.aws_lambda as _lambda
from os import PathLike
from pathlib import Path
from json import loads, dumps
from typing import Self


class OpenApiParser(dict):
    @classmethod
    def from_file(cls, path: PathLike) -> Self:
        if not isinstance(path, Path):
            path = Path(path)
        return cls(loads(path.read_text()))

    def add_function(self, f: _lambda.Function) -> Self:
        arn = str(f.function_arn)
        for path, methods in self.get("paths", {}).items():
            for method, _ in methods.items():
                methods[method]["x-amazon-apigateway-integration"] = {
                    "uri": arn,
                    "httpMethod": method.upper(),
                    "payloadFormatVersion": "1.0",
                }
        return self

    def add_auth(self, auth: Auth) -> Self:
        auth_value = auth.get_open_api_auth()
        if auth_value:
            for path, methods in self.get("paths", {}).items():
                for method, value in methods.items():
                    methods[method] = {**value, **auth_value}
        return self

    def save(self, path: PathLike) -> Self:
        if not isinstance(path, Path):
            path = Path(path)
        path.write_text(dumps(self, indent=2))
        return self
