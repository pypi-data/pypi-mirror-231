from abc import ABC, abstractmethod
import aws_cdk.aws_apigateway as apigw


class Auth(ABC):
    @abstractmethod
    def get_open_api_auth(self) -> dict[str, dict]:
        ...

    @abstractmethod
    def get_auth_type(self) -> apigw.AuthorizationType:
        ...


class NoAuth(Auth):
    def get_open_api_auth(self) -> dict[str, dict]:
        return {}

    def get_auth_type(self) -> apigw.AuthorizationType:
        return apigw.AuthorizationType.NONE


class IAMAuth(Auth):
    def get_open_api_auth(self) -> dict[str, dict]:
        return {
            "x-amazon-apigateway-auth": {
                "type": "AWS_IAM",
            }
        }

    def get_auth_type(self) -> apigw.AuthorizationType:
        return apigw.AuthorizationType.IAM


class CognitoAuth(Auth):
    def __init__(self, user_pool_arn: str, user_pool_client_id: str):
        self.user_pool_arn = user_pool_arn
        self.user_pool_client_id = user_pool_client_id

    def get_open_api_auth(self) -> dict[str, dict]:
        return {
            "x-amazon-apigateway-auth": {
                "type": "COGNITO_USER_POOLS",
                "providerARNs": [self.user_pool_arn],
            }
        }

    def get_auth_type(self) -> apigw.AuthorizationType:
        return apigw.AuthorizationType.COGNITO

