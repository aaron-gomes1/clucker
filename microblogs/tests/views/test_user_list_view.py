""""Test of the user list view"""
from django.contrib import messages
from django.test import TestCase
from django.urls import reverse
from microblogs.forms import UserListForm
from microblogs.models import User
from django.contrib.auth import get_user_model
from microblogs.tests.helpers import reverse_with_next


class UserListTestCase(TestCase):
    """Test of the user list view"""

    fixtures = ['microblogs/tests/fixtures/default_user.json']

    def setUp(self):
        self.url = reverse('users')
        self.user = User.objects.get(username='@johndoe')

    def test_user_list_url(self):
        self.assertEqual(self.url, '/users/')

    def test_get_user_list(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')

    def test_get_user_list_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)
