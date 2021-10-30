import os

configuration = {
    'DATABASE_URL': os.environ.get('DATABASE_URL'),
    'SCRAP_URL': 'https://fundamentus.com.br/resultado.php'
}
