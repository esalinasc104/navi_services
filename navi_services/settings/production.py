from navi_services.settings.common import *
from _socket import gethostname

DEBUG = False

ALLOWED_HOSTS = [gethostname(), "*"]
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'navi',
        'HOST': 'mongodb+srv://navi:o6wJQCdnPEccwuPg@diez-cuatro-blwgr.mongodb.net/admin?retryWrites=true&w=majority',
        'USER': 'navi',
        'PASSWORD': 'o6wJQCdnPEccwuPg',
    }
}
