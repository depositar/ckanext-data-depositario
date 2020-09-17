from setuptools import setup, find_packages
import sys, os

version = '6.4.2b'

entry_points = {
    'ckan.plugins': [
	'data_depositario = ckanext.data_depositario.plugin:DataDepositarioDatasets',
        'depositar_iso639 = ckanext.data_depositario.plugin:DepositarISO639'
    ],
    'babel.extractors': [
        'ckan = ckan.lib.extract:extract_ckan',
    ],
}

setup(
    name='ckanext-data-depositario',
    version=version,
    description="CKAN extension for depositar",
    long_description='''
    ''',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='CKAN',
    author='Cheng-Jen Lee',
    author_email='u103133.u103135@gmail.com',
    url='https://github.com/depositar-io/ckanext-data-depositario',
    license='MIT',
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
            ('**/fanstatic/scripts/vendor/**.js', 'ignore', None),
            ('**.js', 'javascript', None),
            ('**/templates/user/new_user_form.html', 'ignore', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
