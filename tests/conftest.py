import os

import mock
import django
from factory import DjangoModelFactory


def pytest_addoption(parser):
    parser.addoption('--postgres', action='store_true')
    parser.addoption(
        '--deprecation', choices=['strict', 'log', 'none'], default='log')


def pytest_configure(config):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

    if config.getoption('postgres'):
        os.environ['DATABASE_ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        os.environ['DATABASE_NAME'] = 'oscar_wagtail'

    django.setup()


def pytest_runtest_setup(item):
    # Patch django-factoryboy since we don't allow db access
    if not item.get_marker('django_db'):
        next_seq_mock = mock.Mock()
        next_seq_mock.return_value = 1

        mock_setup_next_sequence = mock.patch.object(
            DjangoModelFactory, '_setup_next_sequence', next_seq_mock)
        mock_setup_next_sequence.start()

        # Disable log_pprint to ignore repr() calls on objects
        mock_log_pprint = mock.patch('factory.utils.log_pprint')
        mock_log_pprint.start()

        def fin():
            mock_setup_next_sequence.stop()
            mock_log_pprint.stop()

        item.addfinalizer(fin)
