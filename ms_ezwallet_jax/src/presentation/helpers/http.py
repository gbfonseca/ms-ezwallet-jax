from ms_ezwallet_jax.src.presentation.protocols.http import HttpResponse


def ok(data: any) -> HttpResponse:
    return {
        'status_code': 200,
        'body': data
    }


def server_error():
    return {
        'status_code': 500,
        'body': Exception('Internal Server Error')
    }
