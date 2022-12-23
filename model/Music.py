from datetime import date

class Music():
    name: str = None
    artist: str = None
    published_at: date = None

    def create(self, name: str, artist: str, published_at: str) -> object:
        pass

    def all(self) -> list:
        pass

    def get(self, name: str) -> object:
        pass