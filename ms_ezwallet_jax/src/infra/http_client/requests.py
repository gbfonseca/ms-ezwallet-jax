from ms_ezwallet_jax.src.domain.usecases.http_client import HttpClient


class RequestsAdapter(HttpClient):

    def get(self, url: str) -> any:
        if(url is None):
            return Exception('Url obrigatória.')
        return
