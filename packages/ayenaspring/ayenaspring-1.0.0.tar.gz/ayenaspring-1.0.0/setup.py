from setuptools import setup, find_packages

setup(
name='ayenaspring',
version='1.0.0', 
author='liangliang137',
author_email='1102071917@qq.com',
url='https://github.com/openai/openai-python',
description='run_package',
long_description='run_ayena_package',
packages=find_packages(),
install_requires=['requests', 'aiohttp', 'typing-extensions', 'tqdm','urllib3==1.26.15'],
python_requires='>=3.7')
