# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cjwt']

package_data = \
{'': ['*']}

install_requires = \
['pyjwt>=2.6.0,<3.0.0']

entry_points = \
{'console_scripts': ['cjwt = cjwt.__main__:main']}

setup_kwargs = {
    'name': 'cjwt',
    'version': '0.2.0',
    'description': 'Simple JWT reader utility',
    'long_description': "# Cat JWT\n\n[![PyPI version](https://badge.fury.io/py/cjwt.svg)](https://badge.fury.io/py/cjwt)\n\n## Install\n\n`pip3 install cjwt`\n\n## Usage\n\n```\nusage: cjwt [-h] [--secret [SECRET]] [file]\n\npositional arguments:\n  file\n\noptions:\n  -h, --help         show this help message and exit\n  --secret [SECRET]  JWT secret\n```\n\n## Examples\n\n### Read header and claims\n\n- Read from stdin\n\n```bash\n$ echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJ0ZXN0IjoiYWJjZGVmIn0.tPJ7bVKyF_FMFQaRT6n7dvhEBnyiBRGhVlwacTsy0mI' | cjwt\nalg: HS256\ntyp: JWT\nsub: 1234567890\nname: John Doe\niat: 1516239022\ntest: abcdef\n```\n\n- Read from file\n\n```bash\n$ cjwt /tmp/jwt.txt\nalg: HS256\ntyp: JWT\nsub: 1234567890\nname: John Doe\niat: 1516239022\ntest: abcdef\n```\n\n- Read from .roadtools_auth\n\n```bash\n$ cat .roadtools_auth | cjwt\ntyp: JWT\nnonce: <cut>\nalg: <cut>\nx5t: <cut>\nkid: <cut>\naud: https://graph.microsoft.com/\n<snip>\n```\n\n### Verify secret\n\n```\necho 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJ0ZXN0IjoiYWJjZGVmIn0.tPJ7bVKyF_FMFQaRT6n7dvhEBnyiBRGhVlwacTsy0mI' | cjwt --secret 'secret'\nalg: HS256\ntyp: JWT\nsub: 1234567890\nname: John Doe\niat: 1516239022\ntest: abcdef\n```\n\n```\necho 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJ0ZXN0IjoiYWJjZGVmIn0.tPJ7bVKyF_FMFQaRT6n7dvhEBnyiBRGhVlwacTsy0mI' | cjwt --secret 'not-secret'\nalg: HS256\ntyp: JWT\nSignature verification failed\n```\n",
    'author': 'Max Harley',
    'author_email': 'maxh@maxh.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
