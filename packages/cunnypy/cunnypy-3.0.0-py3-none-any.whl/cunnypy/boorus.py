import os
from dataclasses import dataclass
from typing import NamedTuple, Self

import anyio
import httpx

from cunnypy.errors import BooruNotFoundError, CunnyPyError, CunnyPyHTTPError


@dataclass(frozen=True, eq=False)
class Post:
    """Dataclass to represent a post on a booru.

    Attributes:
        post_id (int): The unique identifier of the post.
        md5 (str): The MD5 hash of the post file.
        rating (str): The rating of the post (e.g. safe, questionable, explicit).
        file_url (str): The URL of the post file.
        sample_url (str): The URL of the post sample file.
        preview_url (str): The URL of the post preview file.
        tags (str): A string of tags associated with the post.
        source (str | None, optional): The source URL of the post (if available).
    """

    post_id: int
    md5: str
    rating: str
    file_url: str
    sample_url: str
    preview_url: str
    tags: list[str]
    source: str | None

    async def download(self: Self, path: os.PathLike[str] | str, file_name: str | None = None) -> os.PathLike[str]:
        """Download the current post.

        Args:
            path (os.PathLike[str] | str): Location to download image
            file_name (str, optional): Name of the file. Defaults to file's hash.

        Raises:
            CunnyPyHTTPError: Raised when failing to fetch file.
            CunnyPyError: Raised when failing to write file.

        Returns:
            os.PathLike[str]: Path location the post was saved to.
        """
        file_name = file_name if file_name else self.md5
        client = httpx.AsyncClient(headers={"User-Agent": "Cunnypy/v3.0.0 (https://pypi.org/project/cunnypy)"})

        async with client as c:
            try:
                res = await c.get(self.file_url)
                res.raise_for_status()

                file_name = f"{file_name}.{res.headers['content-type'].split('/')[-1]}"
                path = await anyio.Path(path).absolute() / file_name

                async with await anyio.open_file(path, "wb") as f:
                    await f.write(res.content)
                    return path
            except (httpx.HTTPStatusError, os.error) as e:
                if isinstance(e, httpx.HTTPStatusError):
                    raise CunnyPyHTTPError(e.__str__(), request=e.request, response=e.response) from None
                raise CunnyPyError("Failed to write file") from e


class Booru(NamedTuple):
    """Class to use when searching with `multi_search` for credential support.

    Args:
        name (str): Name or alias of the booru to search.
        credentials (dict[str, str], optional): Api credentials of the booru. Defaults to None.
    """

    name: str
    credentials: dict[str, str] | None = None


class _API(NamedTuple):
    page: str
    auto: str


class _Site(NamedTuple):
    name: str
    post_api: str
    auto_api: str
    api_vars: _API


_BOORUS = {
    # AllTheFallen
    ("allthefallen", "atfbooru", "atf"): {
        "post_api": "https://booru.allthefallen.moe/posts.xml",
        "auto_api": "https://booru.allthefallen.moe/tags?commit=Search&search[hide_empty]=yes&search[order]=count",
        "api_vars": _API("page", "search[name_or_alias_matches]"),
    },
    # E621
    ("e621", "e6"): {
        "post_api": "https://e621.net/posts.json",
        "auto_api": "https://e621.net/tags.json/?search[order]=count",
        "api_vars": _API("page", "search[name_matches]"),
    },
    # E926
    ("e926", "e9"): {
        "post_api": "https://e926.net/posts.json",
        "auto_api": "https://e926.net/tags.json/?search[order]=count",
        "api_vars": _API("page", "search[name_matches]"),
    },
    # Danbooru
    ("danbooru", "dan", "db"): {
        "post_api": "https://danbooru.donmai.us/posts.xml",
        "auto_api": "https://danbooru.donmai.us/tags?commit=Search&search[hide_empty]=yes&search[order]=count",
        "api_vars": _API("page", "search[name_or_alias_matches]"),
    },
    # Gelbooru
    ("gelbooru", "gel", "gb"): {
        "post_api": "https://gelbooru.com/index.php?page=dapi&s=post&q=index",
        "auto_api": "https://gelbooru.com/index.php?page=tags&s=list&sort=desc&order_by=index_count",
        "api_vars": _API("pid", "tags"),
    },
    # Hypnohub
    ("hypnohub", "hh", "hypno"): {
        "post_api": "https://hypnohub.net/index.php?page=dapi&s=post&q=index",
        "auto_api": "https://hypnohub.net/index.php?page=tags&s=list&sort=desc&order_by=index_count",
        "api_vars": _API("pid", "tags"),
    },
    # Konachan
    ("konachan", "kc", "kona"): {
        "post_api": "https://konachan.com/post.xml",
        "auto_api": "https://konachan.com/tag.xml/?order=count",
        "api_vars": _API("page", "name"),
    },
    # Konachan.net
    ("konanet", "kcn"): {
        "post_api": "https://konachan.net/post.xml",
        "auto_api": "https://konachan.net/tag.xml/?order=count",
        "api_vars": _API("page", "name"),
    },
    # Lolibooru
    ("lolibooru", "loli", "lb"): {
        "post_api": "https://lolibooru.moe/post/index.xml",
        "auto_api": "https://lolibooru.moe/tag/index.xml/?order=count",
        "api_vars": _API("page", "name"),
    },
    # Rule34
    ("rule34", "r34"): {
        "post_api": "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index",
        "auto_api": "https://rule34.xxx/index.php?page=tags&s=list&sort=desc&order_by=index_count",
        "api_vars": _API("pid", "tags"),
    },
    # Safebooru
    ("safebooru", "safe", "sb"): {
        "post_api": "https://safebooru.org/index.php?page=dapi&s=post&q=index",
        "auto_api": "https://safebooru.org/index.php?page=tags&s=list&sort=desc&order_by=index_count",
        "api_vars": _API("pid", "tags"),
    },
    # Tbib
    ("tbib", "tb"): {
        "post_api": "https://tbib.org/index.php?page=dapi&s=post&q=index",
        "auto_api": "https://tbib.org/index.php?page=tags&s=list&sort=desc&order_by=index_count",
        "api_vars": _API("pid", "tags"),
    },
    # Xbooru
    ("xbooru", "xb"): {
        "post_api": "https://xbooru.com/index.php?page=dapi&s=post&q=index",
        "auto_api": "https://xbooru.com/index.php?page=tags&s=list&sort=desc&order_by=index_count",
        "api_vars": _API("pid", "tags"),
    },
    # Yande.re
    ("yandere", "yan"): {
        "post_api": "https://yande.re/post.xml",
        "auto_api": "https://yande.re/tag.xml/?order=count",
        "api_vars": _API("page", "name"),
    },
}


async def _getbooru(booru: str) -> _Site:
    for names, api in _BOORUS.items():
        if booru in names:
            return _Site(names[0], **api)  # type: ignore[arg-type]

    raise BooruNotFoundError(booru)
