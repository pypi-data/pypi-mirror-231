# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eaot']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'eaot',
    'version': '0.0.1',
    'description': 'Paper - Pytorch',
    'long_description': "[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers\nAgora's open source implementation of the paper: Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers\n\n[PAPER LINK](https://arxiv.org/pdf/2309.08532.pdf)\n\n## Installation\n\nYou can install the package using pip\n\n# Citation\n```BibTeX\n@misc{2309.08532,\nAuthor = {Qingyan Guo and Rui Wang and Junliang Guo and Bei Li and Kaitao Song and Xu Tan and Guoqing Liu and Jiang Bian and Yujiu Yang},\nTitle = {Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers},\nYear = {2023},\nEprint = {arXiv:2309.08532},\n}\n```",
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/eaot',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
