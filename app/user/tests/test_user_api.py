"""
This module test user api
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("user:create")
LOGIN_USER_URL = reverse("user:login")
TOKEN_URL = reverse("user:token")
ME_URL = reverse("user:me")


def create_user(**params):
    """
    Helper function to create a user
    """

    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """
    Test the user API (public)
    """

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """
        Test creating user with valid payload is successful
        """

        payload = {
            "email": "test@example.com",
            "password": "password123",
            "fullname": "Test User",
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_login_user_success(self):
        """
        Test logging in user with valid credentials is successful
        """

        payload = {
            "email": "test@example.com",
            "password": "password123",
        }
        create_user(**payload)
        res = self.client.post(LOGIN_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        user = get_user_model().objects.get(email=payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertIn("token", res.data)

    def test_user_exists(self):
        """
        Test creating a user that already exists fails
        """

        payload = {
            "email": "test@example.com",
            "password": "password123",
            "fullname": "Test User",
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """
        Test that the password must be more than 5 characters
        """

        payload = {
            "email": "test@example.com",
            "password": "pw",
            "fullname": "Test User",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """
        Test that a token is created for the user
        """

        user_details = {
            "fullname": "Test User",
            "email": "test@example.com",
            "password": "password123",
        }
        create_user(**user_details)
        payload = {
            "email": user_details["email"],
            "password": user_details["password"],
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """
        Test that token is not created if invalid credentials are given
        """

        create_user(email="test@example.com", password="password123")
        payload = {
            "email": "test@example.com", "password": "wrongpassword"}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """
        Test that token is not created if password is blank
        """

        payload = {
            "email": "test@example.com", "password": ""}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """
        Test that token is not created if user does not exist
        """

        payload = {
            "email": "test@example.com", "password": "password123"}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """
        Test that authentication is required for users
        """

        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """
    Test API requests that require authentication
    """

    def setUp(self):
        self.user = create_user(
            email="test@example.com", password="password123", fullname="Test User")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """
        Test retrieving profile for logged in user
        """

        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            "email": self.user.email,
            "fullname": self.user.fullname
        })

    def test_post_me_not_allowed(self):
        """
        Test that POST is not allowed on the me url
        """

        res = self.client.post(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """
        Test updating the user profile for authenticated user
        """

        payload = {"fullname": "New Name", "password": "newpassword123"}
        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.fullname, payload["fullname"])
        self.assertTrue(self.user.check_password(payload["password"]))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
