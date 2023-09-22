from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

KEYWORDS = ('Argparse,jsonschema,Argument Schema,'
            'data validation, json, validation,'
            'command, line, parser, parsing')

name = 'argparse-from-jsonschema'
module = name.replace("-", "_")
setup(
    name=name,
    version='0.0.6',
    description='Parse Argument with JSON Schema',
    url=f'https://github.com/LeConTesteur/{name}',
    author='LeConTesteur',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=KEYWORDS,
    entry_points={
        'console_scripts': [f'{name}={module}:main'],
    },
    py_modules=[f'{module}']
)
