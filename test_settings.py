import atexit
import shutil
import tempfile

from foundry.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'test_foundry.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

def _tempdir():
    """
    Return the path to a new directory that will be deleted on process exit.
    """
    path = tempfile.mkdtemp(prefix='jmbo-foundry-test-')
    atexit.register(shutil.rmtree, path, ignore_errors=True)
    return path

CKEDITOR_UPLOAD_PATH = _tempdir()
