"""4_Dod ex02"""

from typing import Any


def callLimit(limit: int):
    """Decorator"""
    count = 0

    def callLimiter(function):
        """applying decorator to the function"""

        def limit_function(*args: Any, **kwds: Any):
            """Checking conditions"""
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call to many times")
        return limit_function
    return callLimiter
