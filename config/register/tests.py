from django.contrib.auth.hashers import check_password, make_password
from django.urls import reverse
from rest_framework.test import APITestCase

from register.serializers import RegisterSerializer
from store.models import User


class RegisterSerializerTest(APITestCase):
    def test_register_serializer_hashes_password_and_sets_client_role(self):
        serializer = RegisterSerializer(
            data={
                'name': 'Ali',
                'phone': '998901234501',
                'email': 'ali1@example.com',
                'password': '12345',
                'password2': '12345',
            }
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()

        self.assertEqual(user.name, 'Ali')
        self.assertEqual(user.phone, '998901234501')
        self.assertEqual(user.role, 'client')
        self.assertTrue(check_password('12345', user.password))

    def test_register_serializer_rejects_password_mismatch(self):
        serializer = RegisterSerializer(
            data={
                'name': 'Ali',
                'phone': '998901234502',
                'email': 'ali2@example.com',
                'password': '12345',
                'password2': '54321',
            }
        )

        self.assertFalse(serializer.is_valid())
        self.assertIn('Passwords must match', str(serializer.errors))


class AuthApiTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_endpoint_creates_user(self):
        payload = {
            'name': 'Ali',
            'phone': '998901234503',
            'email': 'ali3@example.com',
            'password': '12345',
            'password2': '12345',
        }

        response = self.client.post(self.register_url, payload, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(phone='998901234503')
        self.assertTrue(check_password('12345', user.password))
        self.assertEqual(user.role, 'client')
        self.assertNotIn('password', response.data)

    def test_login_endpoint_returns_success_for_valid_credentials(self):
        User.objects.create(
            name='Ali',
            phone='998901234504',
            email='ali4@example.com',
            password=make_password('12345'),
            role='client',
        )

        response = self.client.post(
            self.login_url,
            {'phone': '998901234504', 'password': '12345'},
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Login successful')
        self.assertEqual(response.data['user']['phone'], '998901234504')

    def test_login_endpoint_rejects_wrong_password(self):
        User.objects.create(
            name='Ali',
            phone='998901234505',
            email='ali5@example.com',
            password=make_password('12345'),
            role='client',
        )

        response = self.client.post(
            self.login_url,
            {'phone': '998901234505', 'password': 'wrong-password'},
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], "Telefon yoki parol noto'g'ri")
