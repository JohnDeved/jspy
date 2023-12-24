from typing import Any

def test(*args: tuple[Any, ...]):
    print("hello from py", *args)
    return 42