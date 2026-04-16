from django.test import TestCase

from store.models import User


class UserModelTest(TestCase):
    def test_user_str_returns_name(self):
        user = User.objects.create(
            name='Ali',
            phone='998901234500',
            email='ali@example.com',
            password='plain-password',
            role='client',
        )

        self.assertEqual(str(user), 'Ali')
        self.assertEqual(User.objects.count(), 1)
