from setuptools import setup, find_packages

setup(
    name='drf-swagger-utils',
    version='1.0.2',
    description='Your package description',
    author='Chinni Raja Ammela',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create_app = drf_swagger_utils.management.commands.create_app:main',
            'build = drf_swagger_utils.management.commands.build:main'
        ],
    }
)
