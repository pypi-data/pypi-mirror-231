# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bovine_herd',
 'bovine_herd.server',
 'bovine_herd.utils',
 'bovine_herd.utils.test']

package_data = \
{'': ['*'], 'bovine_herd.server': ['templates/*']}

install_requires = \
['bovine-process>=0.4.0,<0.5.0', 'bovine-store>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'bovine-herd',
    'version': '0.4.0',
    'description': 'Implementation of a Fediverse server based on bovine',
    'long_description': '# bovine_herd\n\n`bovine_herd` is a `bovine` powered ActivityPub server, which interoperates with the rest of the FediVerse.\n\nRunning:\n\n```bash\npip install bovine_herd\nhypercorn bovine_herd:app\n```\n\nThis will start `bovine_herd` using an sqlite3 database.\n\n## Interacting with the fediverse\n\nAssume that you alias `$DOMAIN` so that it redirects to the above server. Then by running\n\n```bash\npip install bovine_tool\npython -mbovine_tool.register --domain $DOMAIN moocow\n```\n\nyou create a new account for __moocow__. This command returns its bovine name, which will be of the form `moocow + uuid4()`, e.g. `moocow_09c80006-483c-4826-b48c-cf5134b4e898`. By running:\n\n```bash\npython -mbovine_tool.manage --new_did_key $BOVINE_NAME\n```\n\nyou will be given a secret (an Ed25519 private key, i.e. starts with `z3u2`). Once you have this secret, you can send a message via\n\n```bash\npython -mbovine.msg --secret $SECRET --host $DOMAIN moooo\n```\n\n## Configuration\n\nThe default database connection is "sqlite://bovine.sqlite3". This can be overwridden with the environment variable "BOVINE_DB_URL".\n\n- `BOVINE_REDIS` represents how to reach redis, e.g. `redis://localhost`. If not set, redis is not used. Redis is necessary when using more than one worker.\n',
    'author': 'Helge',
    'author_email': 'helge.krueger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/bovine/bovine',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
