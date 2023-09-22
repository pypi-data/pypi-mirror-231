# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fmn',
 'fmn.api',
 'fmn.api.handlers',
 'fmn.backends',
 'fmn.cache',
 'fmn.consumer',
 'fmn.core',
 'fmn.database',
 'fmn.database.migrations',
 'fmn.database.migrations.versions',
 'fmn.database.model',
 'fmn.messages',
 'fmn.rules',
 'fmn.sender']

package_data = \
{'': ['*']}

install_requires = \
['click-plugins>=1.1.1,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'pydantic-settings>=2.0.2,<3.0.0',
 'python-dotenv>=0.20.0,<2.0.0',
 'sqlalchemy-helpers>=0.11']

extras_require = \
{'api': ['fastapi>=0.78.0,<0.104.0',
         'uvicorn>=0.18.2,<0.24.0',
         'httpx>=0.23.0,<0.26.0',
         'fedora-messaging>=3.3.0,<4.0.0',
         'SQLAlchemy>=1.4.41,<3.0.0',
         'httpx-gssapi>=0.1.7,<0.2.0',
         'backoff>=2.2.1,<3.0.0',
         'cashews[redis]>=5.1.0,<7.0.0'],
 'consumer': ['fedora-messaging>=3.3.0,<4.0.0',
              'aio-pika>=8.2.0,<10.0.0',
              'SQLAlchemy>=1.4.41,<3.0.0',
              'backoff>=2.2.1,<3.0.0',
              'cashews[redis]>=5.1.0,<7.0.0'],
 'database': ['alembic>=1.8.1,<2.0.0', 'SQLAlchemy>=1.4.41,<3.0.0'],
 'postgresql': ['psycopg2>=2.9.3,<3.0.0', 'asyncpg>=0.26.0,<0.29.0'],
 'schemas': ['anitya-schema',
             'bodhi-messages',
             'ci-messages',
             'copr-messaging',
             'discourse2fedmsg-messages',
             'fedocal-messages',
             'fedorainfra-ansible-messages',
             'fedora-elections-messages',
             'fedora-messaging-the-new-hotness-schema',
             'fedora-planet-messages',
             'koji-fedoramessaging-messages',
             'mdapi-messages',
             'noggin-messages',
             'nuancier-messages',
             'pagure-messages',
             'mediawiki-messages',
             'koschei-messages'],
 'sender-email': ['tomli>=2.0.1,<3.0.0',
                  'aio-pika>=8.2.0,<10.0.0',
                  'aiosmtplib>=1.1.6,<3.0.0'],
 'sender-irc': ['tomli>=2.0.1,<3.0.0',
                'aio-pika>=8.2.0,<10.0.0',
                'irc>=20.1.0,<21.0.0'],
 'sender-matrix': ['tomli>=2.0.1,<3.0.0',
                   'aio-pika>=8.2.0,<10.0.0',
                   'matrix-nio>=0.20.1,<0.22.0'],
 'sqlite': ['aiosqlite>=0.17.0,<0.20.0']}

entry_points = \
{'console_scripts': ['fmn = fmn.core.cli:cli',
                     'fmn-sender = fmn.sender.cli:main'],
 'fedora.messages': ['fmn.rule.create.v1 = fmn.messages.rule:RuleCreateV1',
                     'fmn.rule.delete.v1 = fmn.messages.rule:RuleDeleteV1',
                     'fmn.rule.update.v1 = fmn.messages.rule:RuleUpdateV1'],
 'fmn.cli': ['api = fmn.api.cli:api',
             'cache = fmn.cache.cli:cache_cmd',
             'database = fmn.database.cli:database'],
 'fmn.filters': ['applications = fmn.rules.filter:Applications',
                 'my_actions = fmn.rules.filter:MyActions',
                 'severities = fmn.rules.filter:Severities',
                 'topic = fmn.rules.filter:Topic'],
 'fmn.tracking_rules': ['artifacts-followed = '
                        'fmn.rules.tracking_rules:ArtifactsFollowed',
                        'artifacts-group-owned = '
                        'fmn.rules.tracking_rules:ArtifactsGroupOwned',
                        'artifacts-owned = '
                        'fmn.rules.tracking_rules:ArtifactsOwned',
                        'related-events = '
                        'fmn.rules.tracking_rules:RelatedEvents',
                        'users-followed = '
                        'fmn.rules.tracking_rules:UsersFollowed']}

setup_kwargs = {
    'name': 'fmn',
    'version': '3.2.0',
    'description': 'Fedora Messaging Notifications',
    'long_description': '<!--\nSPDX-FileCopyrightText: Contributors to the Fedora Project\n\nSPDX-License-Identifier: MIT\n-->\n\n# Fedora Messaging Notifications\n\n`fmn` is a family of systems to manage end-user notifications triggered by\n[`fedora-messaging`](https://fedora-messaging.readthedocs.io), it provides a single place for all\napplications using `fedora-messaging` to notify users of events.\n',
    'author': 'Aurélien Bompard',
    'author_email': 'aurelien@bompard.org',
    'maintainer': 'Aurélien Bompard',
    'maintainer_email': 'aurelien@bompard.org',
    'url': 'https://github.com/fedora-infra/fmn',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
