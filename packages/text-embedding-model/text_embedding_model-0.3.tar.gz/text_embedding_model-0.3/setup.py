import os
from setuptools import find_packages
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

metadata = {
    'name': 'text_embedding_model',
    'version': 'v0.3',
    'author': 'David Yang',
    'author_email':'dongjunyang29@gmail.com',
    'maintainer': 'David Yang',
    'maintainer_email': 'david.b.yang@au.pwc.com',
    'description': 'text_similarity_model',
    'long_description': long_description,
    'install_requires': requirements,
    'packages': find_packages(),
    'include_package_data': True,
    'package_dir': {'text_embedding_model': 'text_embedding_model'},
}

setup(**metadata)
