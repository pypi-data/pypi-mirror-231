<h1 align="center">🦀 Cunny.py 🦀</h1>
<h3 align="center">🔥A Blazingly Fast Image Board Library🔥</h3>


---

<p align="center">
	<a href="#📥Installation">📥Installation</a> |
	<a href="#🌟Features">🌟Features</a> |
	<a href="#⚙️Usage">⚙️Usage</a>
</p>
<br>

## 📥Installation
✅ Getting started with Cunny.py is quick and easy! Simply install the package using your favorite tool.

📥Using [pip](https://pypi.org/project/pip/):

```bash
pip install cunnypy
```

🪶Using [poetry](https://python-poetry.org):

```bash
poetry add cunnypy
```

## 🌟Features
- 🔥 **Blazingly Fast**™️
- 🐍 **Modern** and **Pythonic** API.
- 🚀 Supports [**AnyIO**](https://github.com/agronholm/anyio), [**AsyncIO**](https://docs.python.org/3/library/asyncio.html), and [**Trio**](https://github.com/python-trio/trio).
- 💯 **15** boorus supported.
- 🆔 Support for **aliases**.
- 🎲 Randomize posts with the `gatcha` parameter.
- 🔍 Autocomplete support for **all** boorus.
- 🔢 Search **any combination** of boors at once.


## ⚙️Usage

### 🔎 Basic Search
📝 **Note**: You can specify additional parameters in the search function.

```python
import asyncio

import cunnypy


async def main():
    posts = await cunnypy.search("gelbooru", "megumin")
    print(posts)

asyncio.run(main())
```

### 🔍 Basic Multi-Booru Search
📝 **Note**: To add credential support import the `Booru` class.
```python
import asyncio

import cunnypy


async def main():
    posts = await cunnypy.ms(["gel", "safe"], "megumin")
    print(posts)

asyncio.run(main())
```

### 🤖 Autocomplete

```python
import asyncio

import cunnypy


async def main():
    auto = await cunnypy.autocomplete("gel", "megumi*")
    print(auto)

asyncio.run(main())
```
