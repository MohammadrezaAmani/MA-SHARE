import os


class Cache:
    "cache htmls"

    def __init__(self) -> None:
        self.db = {}

    def add(self, path, html):
        if not os.path.exists(path):
            return False
        self.db[path] = {"content": html, "lchange": os.path.getctime(path)}
        return True

    def check(self, path):
        if not path in self.db:
            return
        if os.path.getctime(path) != self.db[path]["lchange"]:
            return
        return self.db[path]["content"]


cache = Cache()
