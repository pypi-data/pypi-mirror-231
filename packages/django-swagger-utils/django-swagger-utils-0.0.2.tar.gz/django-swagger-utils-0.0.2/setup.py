from setuptools import setup, find_packages

setup(
    name='django-swagger-utils',
    version='0.0.2',
    description='Your package description',
    author='Chinni Raja Ammela',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'python manage.py = drf_swagger_utils.management.commands.custom_command:Command'
        ],
    }
)
