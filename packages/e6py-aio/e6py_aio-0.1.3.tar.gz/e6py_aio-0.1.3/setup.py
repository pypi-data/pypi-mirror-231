# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['e6py_aio',
 'e6py_aio.http',
 'e6py_aio.http.endpoints',
 'e6py_aio.models',
 'e6py_aio.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=23.2.1,<24.0.0',
 'aiohttp>=3.8.5,<4.0.0',
 'attrs>=22.2.0,<23.0.0',
 'sentinel>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'e6py-aio',
    'version': '0.1.3',
    'description': 'An e621 asyncio API wrapper',
    'long_description': '# e6py-aio\n\n`e6py-aio` is an asyncio API wrapper for e621/e926\n\n## Requirements\n\n- Python >= 3.10\n- aiohttp >= 3.8.5\n- attrs >= 22.2.0\n\n## Usage\n\n```py\nfrom e6py_aio import E621Client\n\nclient = E621Client(login="username", api_key="API Key")\nposts = await client.get_posts()\n\nfor post in posts:\n    print(f"Got post {post.id}")\n    print(f"  Rating: {post.rating}")\n    print(f"   Score: {post.score}")\n    print(f"     URL: {post.file.url}")\n```\n',
    'author': 'zevaryx',
    'author_email': 'zevaryx@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
