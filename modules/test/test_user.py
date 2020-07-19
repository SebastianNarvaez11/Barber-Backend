from django.test import TestCase
from django.contrib.auth import authenticate
from modules.users.models import User


class CreateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_create(self):
        user_one = User.objects.create_user(username='test2', first_name='Juan', last_name='Perez',
                                            role='ADMIN', telephone='3188403067', password='12test12', email='test1@example.com')
        self.assertTrue((user_one is not None))


    def test_confirm_instance(self):
        self.assertTrue(isinstance(self.user, User))

    

class UpdateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_username(self):
        self.user.username = 'test3'
        self.user.save()
        self.assertTrue(self.user.username == 'test3')
    
    def test_change_password(self):
        self.user.set_password('test3')
        self.user.save()
        user_test = authenticate(username='test', password='test3')
        self.assertTrue(user_test.is_authenticated)



class DeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()
    
    def test_update_username(self):
        self.user.delete()
        self.assertFalse(User.objects.filter(username='test').exists())