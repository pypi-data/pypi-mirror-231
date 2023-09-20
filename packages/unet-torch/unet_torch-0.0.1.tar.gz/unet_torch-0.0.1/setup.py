# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unet']

package_data = \
{'': ['*']}

install_requires = \
['torch']

setup_kwargs = {
    'name': 'unet-torch',
    'version': '0.0.1',
    'description': 'unet - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Unet\nMy implemenetation of a modular Unet from the paper "U-Net: Convolutional Networks for Biomedical Image Segmentation"\n\n[Paper Link](https://arxiv.org/abs/1505.04597)\n\n# Appreciation\n* Lucidrains\n* Agorians\n\n\n\n# Install\n`pip install unet`\n\n# License\nMIT\n\n# Citations\n```bibtex\n@misc{1505.04597,\nAuthor = {Olaf Ronneberger and Philipp Fischer and Thomas Brox},\nTitle = {U-Net: Convolutional Networks for Biomedical Image Segmentation},\nYear = {2015},\nEprint = {arXiv:1505.04597},\n}\n```',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/SimpleUnet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
