class Database():
    music_list: list = []

    def add(self, music_object) -> object:
        self.music_list.append(music_object)
        return music_object

    def retrieve(self, music_name: str) -> object:
        for music in self.music_list:
            if music.get('name') == music_name:
                return {'status': 200, 'data': music }
        return {'status': 404, 'data': None }

    def all(self) -> list:
        return self.music_list
