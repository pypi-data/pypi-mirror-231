from .python_version import PythonVersion
from .auth import Auth, NoAuth, CognitoAuth
from .open_api_parser import OpenApiParser
from constructs import Construct
import aws_cdk.aws_apigateway as apigw
import aws_cdk as cdk
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_cognito as cognito
from os import PathLike


class LitestarApp(Construct):
    def __init__(self, scope: Construct, construct_id: str, path: PathLike, handler: str | None = "app.app",
                 runtime: PythonVersion.RUNTIME = None, bundling_opts: cdk.BundlingOptions | None = None,
                 env: dict[str, str] | None = None, memory_size: int = 1024, timeout: int | None = 30,
                 auth: Auth = None, open_api_path: PathLike | None = None):
        super().__init__(scope, construct_id)
        self.path = path
        self.handler = handler
        self.runtime = PythonVersion.check_runtime(runtime) if runtime else PythonVersion.get_runtime()
        self.bundling_opts = bundling_opts or cdk.BundlingOptions(
            image=self.runtime.bundling_image,
            user="root",
            command=[
                "bash",
                "-c",
                "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output",
            ],
        )
        self.env = env or {}
        self.memory_size = memory_size
        self.timeout = timeout
        self.auth = auth or NoAuth()
        self.open_api_path = open_api_path
        self.open_api_parser: OpenApiParser | None = None
        self.function = _lambda.Function(
            self,
            f"{construct_id}Function",
            code=_lambda.Code.from_asset(
                str(self.path),
                bundling=self.bundling_opts,
            ),
            runtime=self.runtime,
            handler=self.handler,
            memory_size=self.memory_size,
            timeout=cdk.Duration.seconds(self.timeout),
            environment=self.env,
        )
        if self.open_api_path:
            self.open_api_parser = OpenApiParser.from_file(self.open_api_path)
            self.open_api_parser.add_function(self.function)
            self.open_api_parser.add_auth(self.auth)
            self.open_api_parser.save(self.open_api_path)
            self.api = apigw.SpecRestApi(
                self,
                f"{construct_id}Api",
                api_definition=apigw.ApiDefinition.from_inline(self.open_api_parser),
            )
        else:
            if isinstance(self.auth, CognitoAuth):
                method_opts = apigw.MethodOptions(
                    authorization_type=self.auth.get_auth_type(),
                    authorizer=apigw.CognitoUserPoolsAuthorizer(
                        self,
                        f"{construct_id}CognitoAuthorizer",
                        cognito_user_pools=[
                            cognito.UserPool.from_user_pool_arn(
                                self,
                                f"{construct_id}CognitoUserPool",
                                self.auth.user_pool_arn,
                            )
                        ],
                    ),
                )
            else:
                method_opts = apigw.MethodOptions(
                    authorization_type=self.auth.get_auth_type(),
                )
            self.api = apigw.LambdaRestApi(
                self,
                f"{construct_id}Api",
                handler=self.function,
                default_method_options=method_opts,
            )
