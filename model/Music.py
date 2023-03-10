from datetime import date, datetime
from database.database import Database

class Music():
    name: str = None
    artist: str = None
    published_at: date = None

    def __init__(self, name=None , artist=None, published_at=None) -> None:
        self.name = name
        self.artist = artist
        self.published_at = published_at

    def __str__(self) -> str:
        return f'{self.name}, {self.artist}, {self.published_at}'

    def save(self) -> object:
        return Database().add({'name': self.name, 'artist': self.artist, 'published_at': self.published_at})

    def all(self) -> list:
        return Database().all()

    def get(self, name: str) -> object:
        return Database().retrieve(name).get('data')

    def filter_by_year(self, year: int) -> object:
        try:
            normalized_year = int(year)
        except ValueError:
            print('Ano invalido!')
            return
        filtered_list = []

        for music in self.all():
            music_publish_year = datetime.strptime(music['published_at'], '%d-%m-%Y').year
            if music_publish_year == normalized_year:
                filtered_list.append(music)
        
        return filtered_list

