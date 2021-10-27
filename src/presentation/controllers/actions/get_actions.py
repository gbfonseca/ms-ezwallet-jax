from src.presentation.protocols.controller import Controller


class GetActions(Controller):
    def __init__(self):
        pass

    def handle(self, http_request):
        return http_request

