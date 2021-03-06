from __future__ import unicode_literals

# pylint: disable=W0401, W0614
from saleor.settings import *  # noqa

SECRET_KEY = 'NOTREALLY'

DEFAULT_CURRENCY = 'USD'

LANGUAGE_CODE = 'en-us'

if 'sqlite' in DATABASES['default']['ENGINE']:
    DATABASES['default']['TEST'] = {  # noqa
        'SERIALIZE': False,
        'NAME': ':memory:',
        'MIRROR': None}
