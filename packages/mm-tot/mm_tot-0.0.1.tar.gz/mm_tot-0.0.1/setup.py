# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tot']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mm-tot',
    'version': '0.0.1',
    'description': 'ToT - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# MultiModal Tree of Thoughts\nMulti-Modal Foundation Model -> Deepfloyd iF or stable diffusion -> mmllm -> if\n\nThe objective is to implement DALLE-3 where given an input task to generate an image => its fed and enriched by the multimodal llm => passed into image generation\n\n\n\n# Appreciation\n* Lucidrains\n* Agorians\n\n\n# Install\n\n# Usage\n\n# Architecture\n\n# Todo\n\n\n# License\nMIT\n\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/MultiModal-ToT',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
