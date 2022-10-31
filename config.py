import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
admin_id = int(os.getenv("ADMIN_ID"))

admins = [227434723]

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
PGHOST = os.getenv('ip')
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}/{DATABASE}'
