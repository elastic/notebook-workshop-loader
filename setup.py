from setuptools import find_packages, setup

setup(
    name='notebookworkshoploader',
    packages=find_packages(),
    description='Notebook Env Loader',
    version='2.0.0',
    author='elastic-sa',
    install_requires=['python-dotenv', 'ipywidgets', 'requests']
)