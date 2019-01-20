from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jms-job-daemon-python-client',
    version='0.0.1',
    description='A Python client for the JMS Job Daemon',
    long_description=long_description,
    url='https://github.com/RUBi-ZA/JMS-Job-Daemon-Python-Client',
    author='David Brown',
    author_email='davidbrownza@outlook.com',
    license='GPLv3',
    packages=['jms'],
    install_requires=[
        'requests',
        'mock'
    ],
    zip_safe=False
)