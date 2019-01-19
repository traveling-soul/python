from django.test import TestCase
from .models import UserInfo

# Create your tests here.
class TestUserInfo(TestCase):
    def setUp(self):
        UserInfo.objects.create(username='老赵', password='123')

    def test_user_info(self):
        user = UserInfo.objects.get(username='老赵')
        self.assertEqual(user.username, '老赵')
        self.assertEqual(user.password, '123')


class TestUserView(TestCase):

    def test_regist(self):
        response = self.client.get('/user/regist/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/user/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_out(self):
        response = self.client.get('/user/login_out/')
        self.assertEqual(response.status_code, 302)






