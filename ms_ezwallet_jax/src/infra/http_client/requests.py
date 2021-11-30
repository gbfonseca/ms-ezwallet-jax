from ms_ezwallet_jax.src.domain.usecases.http_client import HttpClient
import requests


class RequestsAdapter(HttpClient):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def get(self, url: str) -> any:
        if(url is None):
            return Exception('Url obrigatória.')
        data = requests.get(url=url, headers=self.headers)
        return data.json()
