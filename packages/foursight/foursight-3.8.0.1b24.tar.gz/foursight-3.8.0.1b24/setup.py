# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chalicelib_fourfront',
 'chalicelib_fourfront.checks',
 'chalicelib_fourfront.checks.helpers',
 'chalicelib_fourfront.scripts']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2==2.10.1',
 'MarkupSafe==1.1.1',
 'PyJWT>=2.5.0,<3.0.0',
 'benchmark-4dn>=0.5.17,<0.6.0',
 'click>=7.1.2,<8.0.0',
 'dcicutils>=7.8.0,<8.0.0',
 'elasticsearch-dsl>=7.0.0,<8.0.0',
 'elasticsearch>=7.13.4,<8.0.0',
 'foursight-core==4.4.0.1b37',
 'geocoder==1.38.1',
 'gitpython>=3.1.2,<4.0.0',
 'google-api-python-client>=1.7.4,<2.0.0',
 'gspread>=3.6.0',
 'oauth2client>=4.1.3',
 'pytest==5.1.2',
 'pytz>=2020.1,<2021.0',
 'tibanna_ff>=0.22.5']

entry_points = \
{'console_scripts': ['decrypt-accounts-file = '
                     'foursight_core.scripts.decrypt_accounts_file:main',
                     'encrypt-accounts-file = '
                     'foursight_core.scripts.encrypt_accounts_file:main',
                     'publish-to-pypi = '
                     'dcicutils.scripts.publish_to_pypi:main']}

setup_kwargs = {
    'name': 'foursight',
    'version': '3.8.0.1b24',
    'description': 'Serverless Chalice Application for Monitoring',
    'long_description': 'None',
    'author': '4DN-DCIC Team',
    'author_email': 'support@4dnucleome.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
