from platform import python_version
import aws_cdk.aws_lambda as _lambda


class UnsupportedPythonVersion(Exception):
    ...


class PythonVersion:
    RUNTIME = _lambda.Runtime
    VERSION_MAP = {
        "3.11": RUNTIME.PYTHON_3_11,
    }

    @classmethod
    def get_runtime(cls) -> _lambda.Runtime:
        version = cls.VERSION_MAP.get(python_version())
        if version is None:
            raise UnsupportedPythonVersion
        return version

    @classmethod
    def check_runtime(cls, runtime: _lambda.Runtime) -> _lambda.Runtime:
        if runtime not in cls.VERSION_MAP.values():
            raise UnsupportedPythonVersion
        return runtime
