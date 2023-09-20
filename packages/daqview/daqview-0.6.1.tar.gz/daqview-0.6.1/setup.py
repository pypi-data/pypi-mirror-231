# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['daqview', 'daqview.models', 'daqview.views']

package_data = \
{'': ['*']}

install_requires = \
['colour>=0.1,<0.2',
 'h5py>=3.6,<4.0',
 'numexpr>=2.8,<3.0',
 'numpy>=1.22,<2.0',
 'pyqt5>=5.15,<6.0',
 'pyqtgraph>=0.12,<0.13',
 'pyyaml>=6.0,<7.0',
 'scipy>=1.8,<2.0']

entry_points = \
{'console_scripts': ['daqview = daqview:main']}

setup_kwargs = {
    'name': 'daqview',
    'version': '0.6.1',
    'description': 'DAQ Data Analysis Software',
    'long_description': '# DAQview\n\nDAQview is a desktop application for viewing live and historic DAQ data.\n\nIt connects to a DAQd server which can stream it live data from a DAQ system,\nor make a list of historic datasets available for download and viewing.\n\nWritten in Python using PyQt5 and pyqtgraph.\n\nLicensed under the GPL 3.0 license.\n\n## Installation\n\nThe recommended way to install is to use `pipx` to install from the published\nversion on PyPI:\n\n```\npipx install daqview\n```\n\nTo run after installation:\n\n```\n$ daqview\n```\n\n## Development Environment\n\nFirst ensure poetry is installed:\n\n```\n$ pip install --user poetry\n```\n\nThen you should be able to install all dependencies using:\n\n```\n$ poetry install\n```\n\nRun using:\n```\n$ poetry run python -m daqview\n```\n\nRun tests with:\n```\n$ poetry run pytest\n```\n\nRun linters with:\n```\n$ poetry run flake8 daqview\n$ poetry run pylint --rcfile=pylint.rc daqview\n```\n\nGenerally flake8 should always pass cleanly, while pylint is much\nharsher and its output should be checked over for any useful suggestions.\n\n## Release\n\nWhen ready to cut a release, ensure `daqview/__init__.py` has the correct\nversion number at the top, and then make a commit to master. Tag the commit\nwith `release-VERSION`, e.g. `release-0.1.0`, and push the commit and the\ntag to GitLab, which will trigger a release build.\n',
    'author': 'Adam Greig',
    'author_email': 'adam@ael.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
