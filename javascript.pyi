# javascript.pyi

from typing import Any, Callable, Optional

class TaskState:
    sleeping: bool
    def wait(self, seconds: int) -> None: ...
    sleep = wait

class AsyncTask:
    def __init__(self, start: bool = False) -> None: ...

def require(package_name: str, package_version: Optional[str] = None) -> Any: ...

def start(fn: Callable[..., Any]) -> None: ...
def stop(fn: Callable[..., Any]) -> None: ...
def abort(fn: Callable[..., Any], killAfterSeconds: Optional[int] = None) -> None: ...

def On(emitter: Any, eventName: str) -> Callable[..., Any]: ...
def Once(emitter: Any, eventName: str) -> Callable[..., Any]: ...
def off(emitter: Any, eventName: str, handlerFn: Callable[..., Any]) -> None: ...

def eval_js(js_code: str) -> Any: ...