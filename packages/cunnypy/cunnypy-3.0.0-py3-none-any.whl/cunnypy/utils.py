from typing import Any, Literal

import httpx
from anyio import to_thread
from anyio.abc import TaskStatus
from parsel import Selector

from cunnypy.boorus import Post, _Site
from cunnypy.errors import CunnyPyHTTPError

_ENDPOINT = Literal["search", "autocomplete"]


async def _request(endpoint: _ENDPOINT, site: _Site, params: httpx.QueryParams) -> Selector:
    client = httpx.AsyncClient(headers={"User-Agent": "Cunnypy/v3.0.0 (https://pypi.org/project/cunnypy)"})
    endpoint = site.post_api if endpoint == "search" else site.auto_api

    async with client as c:
        try:
            res = await c.get(endpoint, params=params)
            res.raise_for_status()
            return Selector(res.text)
        except httpx.HTTPStatusError as e:
            raise CunnyPyHTTPError(e.__str__(), request=e.request, response=e.response) from None


async def _format_rating(rating: str, site: _Site) -> str:
    match rating:
        case "s":
            if site.name == "danbooru":
                return "sensitive"
            return "safe"
        case "g":
            return "general"
        case "q":
            return "questionable"
        case "e":
            return "explicit"
        case _:
            return rating


async def _create_post(data: Selector, site: _Site, task_status: TaskStatus[Any]) -> None:
    if data.type == "json":
        _data = data.get()
        _data["rating"] = await _format_rating(_data["rating"], site=site)
        return task_status.started(Post(**_data))
    if data.attrib:
        rating = await _format_rating(data.attrib["rating"], site)
        return task_status.started(
            Post(
                int(data.attrib["id"]),
                data.attrib["md5"],
                rating,
                data.attrib["file_url"],
                data.attrib["sample_url"],
                data.attrib["preview_url"],
                data.attrib["tags"].split(" "),
                data.attrib["source"],
            )
        )

    post_id = await to_thread.run_sync(data.xpath, "./id/text()")
    md5 = await to_thread.run_sync(data.xpath, "./md5/text()")
    rating = await to_thread.run_sync(data.xpath, "./rating/text()")
    file_url = await to_thread.run_sync(data.xpath, "./*[name()='file_url' or name()='file-url']/text()")
    sample_url = await to_thread.run_sync(data.xpath, "./*[name()='sample_url' or name()='large-file-url']/text()")
    preview_url = await to_thread.run_sync(data.xpath, "./*[name()='preview_url' or name()='preview-file-url']/text()")
    tags = await to_thread.run_sync(data.xpath, "./*[name()='tags' or name()='tag-string']/text()")
    source = await to_thread.run_sync(data.xpath, "./source/text()")

    return task_status.started(
        Post(
            int(post_id.get()),  # type: ignore[arg-type]
            md5.get(),  # type: ignore[arg-type]
            await _format_rating(rating.get(), site),
            file_url.get(),  # type: ignore[arg-type]
            sample_url.get(),  # type: ignore[arg-type]
            preview_url.get(),  # type: ignore[arg-type]
            tags.get().split(" "),  # type: ignore[arg-type]
            source.get(),
        )
    )
