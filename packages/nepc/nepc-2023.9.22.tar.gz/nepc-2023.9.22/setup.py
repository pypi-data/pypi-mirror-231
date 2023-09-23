# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nepc', 'nepc.curate', 'nepc.mysql', 'nepc.util']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=7.3.0,<8.0.0',
 'ipython_genutils>=0.2.0,<0.3.0',
 'jupyter-client>=8.3.1,<9.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'matplotlib>=3.8.0,<4.0.0',
 'mysql-connector-python>=8.0.17,<9.0.0',
 'numpy>=1.16.2,<2.0.0',
 'pandas>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'nepc',
    'version': '2023.9.22',
    'description': 'Build, access, and explore a NEPC database.',
    'long_description': '# NEPC\n\n![workflow status](https://github.com/USNavalResearchLaboratory/nepc/actions/workflows/main.yml/badge.svg)\n[![Documentation Status](https://readthedocs.org/projects/nepc/badge/?version=latest)](https://nepc.readthedocs.io/en/latest/?badge=latest)\n![GitHub](https://img.shields.io/github/license/USNavalResearchLaboratory/nepc)\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3974315.svg)](https://doi.org/10.5281/zenodo.3974315)\n\nThe goals of the nepc project are to provide tools to:\n\n1. parse, evaluate, and populate metadata for electron scattering cross sections;\n2. build a NEPC MySQL database of cross sections;\n2. curate, access, visualize, and use cross section data from a NEPC database; and\n4. support verification and validation of electron scattering cross section data.\n\nThe database schema and Python module are designed \nfor anyone interested in plasma chemistry with a background in physics at the graduate level.\n\nDocumentation for the nepc project: [https://nepc.readthedocs.io](https://nepc.readthedocs.io).\n\n## Organization\n\nThe project is organized in the following directories:\n\n* tests - unit and integration testing\n* tests/data - data directory for the `nepc_test` database--an example NEPC database containing fictitious electron scattering cross section data used in unit and integration testing\n* tests/data/eda - example exploratory data analysis (EDA) of a NEPC database that is possible with the nepc Python module\n* tests/data/curate - code used to curate fictitious cross section data in [LXCat](https://nl.lxcat.net/data/set_type.php) format and create various NEPC `Model`s for the `nepc_test` database\n* docs - files used by Sphinx to generate the [NEPC documentation](https://nepc.readthedocs.io)\n* nepc - the Python code for the nepc package and building a NEPC database\n* nepc/mysql - the Python code for creating a NEPC database from data in `NEPC_CS_HOME` environment variable; also creates the `nepc_test` database from data in `NEPC_HOME/tests/data` (must have the `NEPC_HOME` environment variable set)\n\n## Getting Started\n\nTo install `nepc` with pip, run:\n\n```shell\n$ pip install nepc\n```\n\nEstablish a connection to the database named `nepc` running on a\nproduction server (you must set an environment variable `NEPC_PRODUCTION` that\npoints to the production server):\n\n```python\n>>> cnx, cursor = nepc.connect()\n```\n\nIf you\'ve built the `nepc_test` database on your local machine \n(see instructions [here](https://nepc.readthedocs.io/en/latest/mysql.html)), establish a connection to it:\n\n```python\n>>> cnx, cursor = nepc.connect(local=True, test=True)\n```\n\nAccess the pre-defined plasma chemistry model, `fict_min2`, in the `nepc_test` database:\n\n```python\n>>> fict_min2 = nepc.Model(cursor, "fict_min2")\n```\n\nPrint a summary of the ``fict_min2`` model, including a stylized Pandas dataframe:\n\n```python\n>>> fict_min2.summary()\n```\n\nPlot the cross sections in `fict_min2`.\n\n```python\n>>> fict_min2.plot(ylog=True, xlog=True, width=8, height=4) \n```\n\nAdditional examples of EDA using nepc are in `tests/data/eda`. Examples of scripts for\ncurating raw data for the `nepc_test` database, including parsing\n[LXCat](https://nl.lxcat.net/data/set_type.php) formatted data,\nare in `tests/data/curate`.\n\n## Built With\n\n*  [Python](https://www.python.org/) \n*  [MySQL](https://www.mysql.com/)\n*  [LaTeX](https://www.latex-project.org/)\n*  [Jupyter Notebook](https://jupyter.org/)\n\n## Pronunciation\n\nNEPC rhymes with the loser of the [Cola War](https://en.wikipedia.org/wiki/Cola_wars).\nIf NEPC were in the\n[CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict),\nits entry would be `N EH P S IY .`.\n\n\n***Approved for public release, distribution is unlimited.***\n',
    'author': 'Paul Adamson',
    'author_email': 'paul@seekingeta.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
