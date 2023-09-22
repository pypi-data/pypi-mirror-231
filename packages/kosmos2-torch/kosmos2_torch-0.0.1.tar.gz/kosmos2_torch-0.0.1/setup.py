# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kosmos']

package_data = \
{'': ['*']}

install_requires = \
['torch', 'zeta']

setup_kwargs = {
    'name': 'kosmos2-torch',
    'version': '0.0.1',
    'description': 'Kosmos - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Kosmos2.5\nMy implementation of Kosmos2.5 from Microsoft research and the paper: "KOSMOS-2.5: A Multimodal Literate Model"\n\n[Paper Link](https://arxiv.org/pdf/2309.11419.pdf)\n\n# Appreciation\n* Lucidrains\n* Agorians\n\n\n\n# Install\n\n\n# Dataset Strategy\nHere is a table summarizing the datasets used in the paper KOSMOS-2.5: A Multimodal Literate Model with metadata and source links:\n\n| Dataset | Modality | # Samples | Domain | Source | \n|-|-|-|-|-|  \n| IIT-CDIP | Text + Layout | 27.6M pages | Scanned documents | [Link](https://ir.nist.gov/cdip/)|\n| arXiv papers | Text + Layout | 20.9M pages | Research papers | [Link](https://arxiv.org/) |  \n| PowerPoint slides | Text + Layout | 6.2M pages | Presentation slides | Web crawl |\n| General PDF | Text + Layout | 155.2M pages | Diverse PDF files | Web crawl |\n| Web screenshots | Text + Layout | 100M pages | Webpage screenshots | [Link](https://www.tensorflow.org/datasets/catalog/c4) |\n| README | Text + Markdown | 2.9M files | GitHub README files | [Link](https://github.com/) |  \n| DOCX | Text + Markdown | 1.1M pages | WORD documents | Web crawl |\n| LaTeX | Text + Markdown | 3.7M pages | Research papers | [Link](https://arxiv.org/) |\n| HTML | Text + Markdown | 6.3M pages | Webpages | [Link](https://www.tensorflow.org/datasets/catalog/c4) |\n\n\n\n# License\nMIT\n\n# Citations\n```bibtex\n@misc{2309.11419,\nAuthor = {Tengchao Lv and Yupan Huang and Jingye Chen and Lei Cui and Shuming Ma and Yaoyao Chang and Shaohan Huang and Wenhui Wang and Li Dong and Weiyao Luo and Shaoxiang Wu and Guoxin Wang and Cha Zhang and Furu Wei},\nTitle = {Kosmos-2.5: A Multimodal Literate Model},\nYear = {2023},\nEprint = {arXiv:2309.11419},\n}\n```\n\n**bold**\n*italics*\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/Kosmos2.5',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
