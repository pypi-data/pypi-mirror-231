from setuptools import setup, find_packages
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]


setup(
    name='snowflake-deployer',
    version='0.1.0',
    description='Snowflake state based deployer',
    author='Justin Hanson, Jernej Plankelj',
    entry_points = {
        'console_scripts': ['snowflake-deployer=src.cli:cli'],
        #'console_scripts': ['snowflake_deployer=src.command_line:cli'],
    },
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
)