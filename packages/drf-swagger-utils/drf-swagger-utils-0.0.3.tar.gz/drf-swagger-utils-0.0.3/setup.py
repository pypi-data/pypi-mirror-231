from setuptools import setup, find_packages

setup(
    name='drf-swagger-utils',
    version='0.0.3',
    description='Your package description',
    author='Chinni Raja Ammela',
    packages=find_packages(),
    install_requires=[
          'django',
    ],
    entry_points={
        'console_scripts': [
            'create_app = drf_swagger_utils.management.commands.create_cleanapp:main',
            'build = drf_swagger_utils.management.commands.build:main'
        ],
    }
)
