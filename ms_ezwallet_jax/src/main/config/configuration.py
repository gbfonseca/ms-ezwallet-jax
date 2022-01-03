import os
from dotenv import load_dotenv

load_dotenv()

configuration = {
    'DATABASE_URL': os.environ.get('DATABASE_URL'),
    'SCRAP_URL': 'https://fundamentus.com.br/resultado.php'
}
