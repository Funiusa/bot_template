import os
from sqlalchemy import URL

BOT_TOKEN = os.environ["BOT_TOKEN"]
PAY_TOKEN = os.environ["PAY_TOKEN"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_USER = os.environ["DATABASE_USER"]
DATABASE_PASSWORD = os.environ["POSTGRES_PASSWORD"]

ADMINS = os.environ["ADMINS"]

base_url = URL.create(
    "postgresql+asyncpg",
    DATABASE_USER,
    DATABASE_HOST,
    DATABASE_NAME,
    int(DATABASE_PORT)
)

# TODO: move in .env
admins_id = ADMINS
