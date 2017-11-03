from setuptools import setup, find_packages
import sys, os

version = '6.0'

entry_points = {
    'ckan.plugins': [
	'data_depositario = ckanext.data_depositario.plugin:DataDepositarioDatasets',
    ],
    'babel.extractors': [
        'ckan = ckan.lib.extract:extract_ckan',
    ],
}

setup(
    name='ckanext-data-depositario',
    version=version,
    description="CKAN extension for data.depositar.io",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Sol Lee',
    author_email='u103133.u103135@gmail.com',
    url='',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=entry_points,
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
