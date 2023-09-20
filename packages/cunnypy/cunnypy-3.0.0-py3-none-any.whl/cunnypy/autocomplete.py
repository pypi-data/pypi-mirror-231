from anyio import to_thread
from httpx import QueryParams

from cunnypy.boorus import _getbooru
from cunnypy.utils import _request


async def autocomplete(booru: str, query: str, *, limit: int = 10) -> list[str]:
    """Get autocompleted tags from the given booru and query.

    * Note: Use `*` as a wildcard

    Args:
        booru (str): Name or alias of the booru to autocomplete from.
        query (str): Tag query to search
        limit (int, optional): Limit of tags to return. Defaults to 10.

    Raises:
        CunnyPyError: Base cunny.py error.

    Returns:
        list[str]: A list of autocompleted tag strings.
    """
    # Try and fetch booru
    site = await _getbooru(booru)

    # Setup vars
    prefix = query[0] if query.startswith("-") else ""
    query = query[1:] if prefix else query
    params = QueryParams({site.api_vars.auto: f"{query}", "limit": limit})

    # Fetch data
    data = await _request("autocomplete", site, params)

    # HTML
    if data.type == "html":
        # Danbooru being special
        _xpath = (
            "//td/a[2][contains(@class, 'tag-type')]/text()"
            if site.name in ("allthefallen", "danbooru")
            else "//span[contains(@class, 'tag-type')]/a/text()"
        )
        tag_list = await to_thread.run_sync(data.xpath, _xpath)
        if len(tag_list) >= 1:
            return [f"{prefix}{t.get()}" for t in tag_list]

    # JSON
    if data.type == "json":
        tag_list = await to_thread.run_sync(data.jmespath, "[*].[name]")
        if len(tag_list) >= 1:
            return [f"{prefix}{t.get()[0]}" for t in tag_list]

    # XML
    tag_list = await to_thread.run_sync(data.xpath, "//tag")
    if len(tag_list) >= 1:
        return [f"{prefix}{t.attrib['name']}" for t in tag_list]

    return []
