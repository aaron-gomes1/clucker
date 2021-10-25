""""Test of the new post view"""
from django.test import TestCase
from django.urls import reverse
from microblogs.forms import PostForm

class NewPostTestCase(TestCase):
    """Test of the new post view"""

    def setUp(self):
        self.url = reverse('new_post')

    def test_new_post_url(self):
        self.assertEqual(self.url, '/new_post/')

    def test_access_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_post.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, PostForm))
        self.assertFalse(form.is_bound)
