# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alembic',
 'alembic.versions',
 'models',
 'models.alembic',
 'models.alembic.versions',
 'models.testing',
 'testing']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.24,<2.0.0',
 'alembic>=1.6.5,<2.0.0',
 'fedora-messaging>=2.1.0',
 'psycopg2>=2.9.1,<3.0.0']

extras_require = \
{'schemas': ['anitya-schema',
             'bodhi-messages',
             'ci-messages',
             'copr-messaging',
             'discourse2fedmsg-messages',
             'fedocal-messages',
             'fedorainfra-ansible-messages',
             'fedora-elections-messages',
             'fedora-messaging-the-new-hotness-schema',
             'fedora-planet-messages',
             'koji-fedoramessaging-messages>=1.2.2,<2.0.0',
             'mdapi-messages',
             'noggin-messages',
             'nuancier-messages',
             'pagure-messages']}

setup_kwargs = {
    'name': 'datanommer-models',
    'version': '1.1.0',
    'description': 'SQLAlchemy models for datanommer',
    'long_description': 'datanommer.models\n=================\n\nThis package contains the SQLAlchemy data model for datanommer.\n\nDatanommer is a storage consumer for the Fedora Infrastructure Message Bus\n(fedmsg).  It is comprised of a `fedmsg <http://fedmsg.com>`_ consumer that\nstuffs every message into a sqlalchemy database.\n',
    'author': 'Fedora Infrastructure',
    'author_email': 'admin@fedoraproject.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fedora-infra/datanommer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
