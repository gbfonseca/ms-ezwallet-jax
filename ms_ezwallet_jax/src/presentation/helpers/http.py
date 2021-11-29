from ms_ezwallet_jax.src.presentation.protocols.http import HttpResponse


def ok(data: any) -> HttpResponse:
    return {
        'status_code': 200,
        'body': data
    }


def bad_request(exception_message: str) -> HttpResponse:
    return {
        'status_code': 400,
        'body': {
            'message': exception_message
        }
    }


def server_error() -> HttpResponse:
    return {
        'status_code': 500,
        'body': Exception('Internal Server Error')
    }
