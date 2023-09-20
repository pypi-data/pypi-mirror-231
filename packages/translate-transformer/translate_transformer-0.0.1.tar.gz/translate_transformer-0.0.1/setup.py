# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tt']

package_data = \
{'': ['*']}

install_requires = \
['shapeless', 'torch']

setup_kwargs = {
    'name': 'translate-transformer',
    'version': '0.0.1',
    'description': 'tt - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Translate Transformer\nA easy, reliable, fluid replication of this pytorch tutorial,\nhttps://pytorch.org/tutorials/beginner/translation_transformer.html\n\n## Installation\n\nYou can install the package using pip\n\n```bash\npip install tt\n```\n\n\n# License\nMIT\n\n\n\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/TranslateTransformer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
