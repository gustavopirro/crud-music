from unittest import TestCase
from database.database import Database
from model.Music import Music
from datetime import datetime


class DatabaseTestCase(TestCase):

    def setUp(self):
        self.test_database = Database()
        
        self.music_mock = { 
            'name': 'Test Music',
            'artist': 'Test Artist',
            'published_at': datetime.now()
        }

    def test_create_new_db_registry(self):
        new_music = self.test_database.add(self.music_mock)
        self.assertEqual(len(self.test_database.music_list), 1)
        self.assertEqual(new_music.get('name'), 'Test Music')
    
    def test_retrieve_registry_from_db(self):
        self.test_database.add(self.music_mock)
        music_obj = self.test_database.retrieve(self.music_mock['name'])
        
        self.assertEqual(music_obj['status'], 200)
        self.assertEqual(music_obj.get('data').get('artist'), 'Test Artist')

    def test_retrieve_invalid_registry_from_db(self):
        music_obj = self.test_database.retrieve('non existent test music name')
        
        self.assertEqual(music_obj['status'], 404)
    
    def test_get_music_db_list(self):
        db_registry_count = len(self.test_database.all())
        self.test_database.add(self.music_mock)
        self.assertEqual(len(self.test_database.all()), db_registry_count + 1)
