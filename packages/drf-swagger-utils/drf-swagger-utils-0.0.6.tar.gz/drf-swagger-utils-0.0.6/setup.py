from setuptools import setup, find_packages

setup(
    name='drf-swagger-utils',
    version='0.0.6',
    description='Your package description',
    author='Chinni Raja Ammela',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create_app = drf_swagger_utils.create_cleanapp:main',
            'build = drf_swagger_utils.build:main'
        ],
    }
)
