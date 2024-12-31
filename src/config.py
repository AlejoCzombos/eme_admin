from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

DATABASE_NAME = config.get("DATABASE_NAME")
DATABASE_HOST = config.get("DATABASE_HOST")
DATABASE_USER = config.get("DATABASE_USER")
DATABASE_PASSWORD = config.get("DATABASE_PASSWORD")

ADMIN_PASSWORD = config.get("ADMIN_PASSWORD")
SECRET = config.get("SECRET")

S3_BUCKET = config.get("S3_BUCKET")
S3_REGION = config.get("S3_REGION")
S3_ACCESS_KEY = config.get("S3_ACCESS_KEY")
S3_SECRET_ACCESS = config.get("S3_SECRET_ACCESS")