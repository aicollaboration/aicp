class OpenApi():
    def __init__(self, path):
        self.path = path
        self.openapi = None
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            self.openapi = f.read()

    def save(self):
        with open(self.path, "w") as f:
            f.write(self.openapi)

    def update(self, data):
        self.openapi = data
        self.save()

    def get(self):
        return self.openapi
