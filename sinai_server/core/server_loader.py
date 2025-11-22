from .di_container import DIContainer

class ServerLoader:
    def __init__(self):
        self.container = DIContainer()

    def get_container(self):
        return self.container
