from typing import Self

from httpx import HTTPStatusError
from httpx._models import Request, Response

__all__ = ("CunnyPyError", "BooruNotFoundError", "CunnyPyHTTPError")


class CunnyPyError(Exception):
    """Base cunny.py error."""


class BooruNotFoundError(CunnyPyError, AttributeError):
    """Error raised when a booru isn't supported."""

    def __init__(self: Self, booru: str) -> None:
        self.message = f"`{booru}` is not a known name or alias of a supported booru."
        super().__init__(self.message)


class CunnyPyHTTPError(CunnyPyError, HTTPStatusError):
    """Error raised when an HTTP Exception happens."""

    def __init__(self: Self, message: str, *, request: Request, response: Response) -> None:
        super().__init__(message, request=request, response=response)
