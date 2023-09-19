# e6py-aio

`e6py-aio` is an asyncio API wrapper for e621/e926

## Requirements

- Python >= 3.10
- aiohttp >= 3.8.5
- attrs >= 22.2.0

## Usage

```py
from e6py_aio import E621Client

client = E621Client(login="username", api_key="API Key")
posts = await client.get_posts()

for post in posts:
    print(f"Got post {post.id}")
    print(f"  Rating: {post.rating}")
    print(f"   Score: {post.score}")
    print(f"     URL: {post.file.url}")
```
