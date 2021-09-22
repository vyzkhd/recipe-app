from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesfull(self):
        """Test creating new user with email"""
        email = "test@london.com"
        password = "testpas123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """test for email normalised"""
        email = 'test@LONDON.com'
        user = get_user_model().objects.create_user(
            email,
            'testpas123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invald_email(self):
        """test creating user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'user123')

    def test_create_new_superuser(self):
        """test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@london.com',
            'testpas123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)