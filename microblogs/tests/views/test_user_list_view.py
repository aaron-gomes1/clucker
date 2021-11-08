""""Test of the user list view"""
from django.contrib import messages
from django.test import TestCase
from django.urls import reverse
from microblogs.forms import UserListForm
from microblogs.models import User
from django.contrib.auth import get_user_model

class UserListTestCase(TestCase):
    """Test of the user list view"""

    def setUp(self):
        self.url = reverse('users')

    def test_user_list_url(self):
        self.assertEqual(self.url, '/users/')

    def test_get_user_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, UserListForm))
        self.assertFalse(form.is_bound)
