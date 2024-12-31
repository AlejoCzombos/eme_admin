import os
from libcloud.storage.providers import get_driver
from libcloud.storage.types import Provider

from libcloud.storage.drivers.local import LocalStorageDriver
from libcloud.storage.drivers.s3 import S3StorageDriver
from sqlalchemy_file.storage import StorageManager

from src.config import S3_ACCESS_KEY, S3_BUCKET, S3_REGION, S3_SECRET_ACCESS

def setup_storage():
    cls = get_driver(Provider.S3)
    driver = cls(S3_ACCESS_KEY, S3_SECRET_ACCESS, region=S3_REGION)
    bucket_banner = driver.get_container(container_name=S3_BUCKET)
    StorageManager.add_storage("default", bucket_banner)
    
    # bucket_banner = driver.get_container(container_name="eme-sitio-web/banners/")
    # bucket_beneficios = driver.get_container(container_name="eme-sitio-web/beneficios/")
    # bucket_general = driver.get_container(container_name="eme-sitio-web/general/")
    
    # StorageManager.add_storage("banners", bucket_banner)
    # StorageManager.add_storage("beneficios", bucket_beneficios)
    # StorageManager.add_storage("general", bucket_general)