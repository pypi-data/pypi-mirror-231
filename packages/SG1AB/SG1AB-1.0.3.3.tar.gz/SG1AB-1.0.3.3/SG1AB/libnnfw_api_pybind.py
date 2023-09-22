# 아키텍처별로 사용할 모듈을 가져옵니다.
import platform
import os
import shutil

#__all__ = ['libnnfw_api_pybind']
# 현재 아키텍처를 확인합니다.
architecture = platform.machine()

if architecture == 'x86_64':
    from .x86_64 import nnfw_api_pybind
elif architecture == 'armv7l':
    from .armv7l import nnfw_api_pybind
elif architecture == 'aarch64':
    from .aarch64 import nnfw_api_pybind
else:
    raise ImportError(f"Unsupported architecture: {architecture}")

def nnfw_session(*args):
    num = len(args)
    if num == 2:
        return libnnfw_api_pybind.nnfw_session(args[0], args[1])
    elif num == 3:
        return libnnfw_api_pybind.nnfw_session(args[0], args[2], args[1])
    else:
        print("Syntax Error")
        return

def tensorinfo():
    return libnnfw_api_pybind.tensorinfo()
