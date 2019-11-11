from navi_services.settings.common import *
from _socket import gethostname

DEBUG = True

ALLOWED_HOSTS = [gethostname(), "*"]
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'navi',
        'HOST': 'ec2-34-220-174-124.us-west-2.compute.amazonaws.com:27017'
    }
}
