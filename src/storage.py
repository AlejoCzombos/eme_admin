import os
from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy_file.storage import StorageManager

def setup_storage():
    os.makedirs("./static/benefits", 0o777, exist_ok=True)
    local_driver = LocalStorageDriver("./static")
    my_container = local_driver.get_container("benefits")

    StorageManager.add_storage("default", my_container)