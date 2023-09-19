# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gen1']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'shapeless', 'torch']

setup_kwargs = {
    'name': 'gen1',
    'version': '0.0.1',
    'description': 'Text to Video synthesis',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n\n# Gen1\nMy Implementation of " Structure and Content-Guided Video Synthesis with Diffusion Models" by RunwayML\n\n\n\n## Citation\n```\n@misc{2302.03011,\nAuthor = {Patrick Esser and Johnathan Chiu and Parmida Atighehchian and Jonathan Granskog and Anastasis Germanidis},\nTitle = {Structure and Content-Guided Video Synthesis with Diffusion Models},\nYear = {2023},\nEprint = {arXiv:2302.03011},\n```\n',
    'author': 'Gen1',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/gen1',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
