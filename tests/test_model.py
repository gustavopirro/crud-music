from unittest import TestCase
from model.Music import Music
from datetime import datetime


class ModelTestCase(TestCase):

    def setUp(self):
        self.music_database = Music()

    def test_create_new_object(self):
        new_music = Music(name='Test Music', artist='Test Artist', published_at=datetime.now())
        new_music.save()

        self.assertIsInstance(new_music, Music)
        self.assertEqual(new_music.name, 'Test Music')
        self.assertEqual(new_music.artist, 'Test Artist')

    def test_get_object(self):
        new_music = Music(name='Test Music', artist='Test Artist', published_at=datetime.now())
        new_music.save()

        music_object = self.music_database.get(name='Test Music')
        self.assertEqual(music_object.get('name'), 'Test Music')