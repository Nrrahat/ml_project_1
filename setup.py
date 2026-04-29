from setuptools import setup, find_packages

def read_requirements(file_path)->list[str]:
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('-e')]

setup(
    name='ml_project_1',
    version='0.0.1',
    author='NRRahat',
    author_email='nrzrahat@gmail.com',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
)