import os
from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy_file.storage import StorageManager

# Configuración del contenedor de almacenamiento
def setup_storage():
    os.makedirs("./static/benefits", 0o777, exist_ok=True)  # Crear directorio si no existe
    local_driver = LocalStorageDriver("./upload_dir")
    my_container = local_driver.get_container("attachment")

    # Registrar el contenedor en el StorageManager
    StorageManager.add_storage("default", my_container)
