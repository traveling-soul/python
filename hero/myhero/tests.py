from django.test import TestCase

# Create your tests here.
class TestHeroView(TestCase):
    def test_index(self):
        response = self.client.get('/myhero/index/')
        self.assertEqual(response.status_code, 200)

    def test_hero(self):
        response = self.client.get('/myhero/hero/')
        self.assertEqual(response.status_code, 200)

    def test_add_handler(self):
        response = self.client.post('/myhero/hero_add_handler/', {'hname': '林平之', 'hage': 24, 'hgender': 1, 'hdesc': '性格多疑', 'hbook_id': 2})
        self.assertEqual(response.status_code, 200)

    def test_edit_handler(self):
        response = self.client.post('/myhero/hero_edit_handler/14', {'hpic': r'‪C:\Users\Administrator\Pictures\林仙儿.jpg'})
        self.assertEqual(response.status_code, 301)

    def test_delete(self):
        response = self.client.post('/myhero/hero_delete/14', {'hpic': r'‪C:\Users\Administrator\Pictures\林仙儿.jpg'})
        self.assertEqual(response.status_code, 301)