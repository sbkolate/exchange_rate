from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='exchange_rate',
    version=version,
    description='Ask for current foreign exchange rates in Sales Order and Quotation',
    author='Systematrix Solutions',
    author_email='kolate.sambhaji@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
