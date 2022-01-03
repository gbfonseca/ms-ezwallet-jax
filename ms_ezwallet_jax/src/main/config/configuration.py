import os
from dotenv import load_dotenv

load_dotenv()

configuration = {
    'DATABASE_URL': os.environ.get('DATABASE_URL'),
    'SCRAP_URL': 'https://fundamentus.com.br/resultado.php',
    'PYTHON_ENV': os.environ.get('PYTHON_ENV'),
    'GOOGLE_CHROME_PATH': os.environ.get('GOOGLE_CHROME_PATH'),
    'CHROMEDRIVER_PATH': os.environ.get('CHROMEDRIVER_PATH')
}
