# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nerf']

package_data = \
{'': ['*']}

install_requires = \
['torch']

setup_kwargs = {
    'name': 'nerf-torch',
    'version': '0.0.1',
    'description': 'Paper - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Nerf\nMy personal implementation of the NERF paper, with much better code. Because the original implementation has ugly code.\n\n\n[Paper Link](https://arxiv.org/abs/2003.08934)\n\n# Appreciation\n* Lucidrains\n* Agorians\n\n\n\n# Install\n`pip install nerf``\n\n# Usage\n\n# Architecture\n\n# Todo\n\n\n# License\nMIT\n\n# Citations\n\n```bibtex\n@misc{2003.08934,\nAuthor = {Ben Mildenhall and Pratul P. Srinivasan and Matthew Tancik and Jonathan T. Barron and Ravi Ramamoorthi and Ren Ng},\nTitle = {NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis},\nYear = {2020},\nEprint = {arXiv:2003.08934},\n}\n```',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/nerf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
