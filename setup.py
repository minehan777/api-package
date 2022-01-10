from glob import glob
from os.path import basename
from os.path import splitext


from setuptools import setup
from setuptools import find_packages

setup(
    name='piyo',
    version='1.0.0',
    author='',
    url='',
    description='',
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=[],
    extras_require={
        'develop' : [],
    }
)