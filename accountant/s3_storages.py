from django.core.files.storage import get_storage_class
from django.utils.functional import SimpleLazyObject

from storages.backends.s3boto import S3BotoStorage


StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')
