import random
from typing import Any, Literal

import anyio
from anyio.abc import TaskStatus
from httpx import QueryParams

from cunnypy.boorus import Booru, Post, _getbooru
from cunnypy.utils import _create_post, _request

_RATING = Literal["safe", "general", "sensitive", "questionable", "explicit"]


async def search(
    booru: str,
    tags: str,
    *,
    limit: int = 10,
    page: int = 1,
    gatcha: bool = False,
    rating: _RATING | None = None,
    credentials: dict[str, str] | None = None,
) -> list[Post]:
    """Main search function for searching boorus.

    Args:
        booru (str): Name or alias of the booru to search.
        tags (str): String of tags to search.
        limit (int, optional): Limit of posts to fetch. Defaults to 10.
        page (int, optional): Page to fetch posts from. Defaults to 1.
        gatcha (bool, optional): Whether to shuffle posts up. Defaults to False.
        rating (str, optional): Rating of posts to request. Defaults to "None" (Meaning any rating).
        credentials (dict[str, str], optional): Api credentials of the booru. Defaults to None.

    Raises:
        CunnyPyError: Base cunny.py error.

    Returns:
        list[Post]: Returns a list of Post objects.

    Example:
    >>> import asyncio
    >>>
    >>> import cunnypy
    >>>
    >>> async def main():
    >>>     posts = await cunnypy.search("gelbooru", "megumin", limit=20, gatcha=True)
    >>>     print(posts)
    >>>
    >>> asyncio.run(main())
    """
    # Try and fetch booru
    site = await _getbooru(booru)

    if rating:
        if rating in ("safe", "general"):
            rating = "general" if site.name == "gelbooru" else "safe"
        tags += f" rating:{rating}"

    # Setup params
    params = QueryParams({"tags": tags, "limit": limit, site.api_vars.page: page, **(credentials or {})})

    # Fetch data
    data = await _request("search", site, params)

    match data.type:
        case "json":
            _jmespath = "posts[*].{post_id: id, md5: file.md5, rating: rating, file_url: file.url, sample_url: sample.url, preview_url: preview.url, tags: tags.[*][][], source: sources[0]}"  # noqa: E501
            post_elements = await anyio.to_thread.run_sync(data.jmespath, _jmespath)
        case _:
            post_elements = await anyio.to_thread.run_sync(data.xpath, "//post")

    # Parse Data
    if len(post_elements) >= 1:
        async with anyio.create_task_group() as tg:
            posts: list[Post] = [await tg.start(_create_post, e, site) for e in post_elements]

            if gatcha and len(posts) > 1:
                await anyio.to_thread.run_sync(random.shuffle, posts)
        return posts
    return []


async def multi_search(
    boorus: list[Booru | str],
    tags: str,
    *,
    limit: int = 10,
    page: int = 1,
    gatcha: bool = False,
    rating: _RATING = "general",
) -> list[Post]:
    """Allows you to search multiple Boorus at once.

    Args:
        boorus (list[Booru | str]): a list of boorus to search. Use `Booru` class for credential support.
        tags (str): String of tags to search.
        limit (int, optional): Limit of posts to fetch. Defaults to 10.
        page (int, optional): Page to fetch posts from. Defaults to 1.
        gatcha (bool, optional): Whether to shuffle posts. Defaults to False.
        rating (str, optional): Rating of posts to request. Defaults to "general".

    Raises:
        CunnyPyError: Base cunny.py error.

    Returns:
        list[Post]: Returns a list of posts.

    Example:
    >>> import asyncio
    >>>
    >>> import cunnypy
    >>>
    >>> async def main():
    >>>     posts = await cunnypy.multi_search(["gb", "r34"], "megumin", page=3)
    >>>     print(posts)
    >>>
    >>> asyncio.run(main())
    """
    posts: list[Post] = []

    # Search task for TaskGroup
    async def _task(booru: Booru | str, task_status: TaskStatus[Any]) -> None:
        _name = booru if not isinstance(booru, Booru) else booru.name
        _creds = None if not isinstance(booru, Booru) else booru.credentials
        return task_status.started(await search(_name, tags, limit=limit, page=page, rating=rating, credentials=_creds))

    # Create TaskGroup
    async with anyio.create_task_group() as tg:
        tasks: list[list[Post]] = [await tg.start(_task, booru) for booru in boorus]

        # Filter posts
        for p_list in tasks:
            if len(p_list) >= 1:
                posts.extend(p_list)

        if gatcha and len(posts) > 1:
            await anyio.to_thread.run_sync(random.shuffle, posts)
        return posts
