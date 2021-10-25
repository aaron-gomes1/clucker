"""Unit tests of the Post form."""

from django.test import TestCase
from django import forms
from microblogs.forms import PostForm
from microblogs.models import User, Post

class PostFormTestCase(TestCase):
    """Unit tests of the Post form."""

    def setUp(self):
        self.form_input = {
            'text': 'Blue sky'
            }

    def test_valid_post_form(self):
        form = PostForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_field(self):
        form = PostForm()
        self.assertIn('text', form.fields)

    def test_text_accepts_valid_input(self):
        input = {'text': "a"*280}
        form = PostForm(data=input)
        self.assertTrue(form.is_valid())

    def test_text_rejects_invalid_input(self):
        input = {'text': "a"*281}
        form = PostForm(data=input)
        self.assertFalse(form.is_valid())

    def test_post_saved_correctly(self):
        input = {'text': "a"*280}
        form = PostForm(data=input)

        user = User.objects.create_user(first_name='Jane', last_name='Doe', username='@janedoe', email='janedoe@example.org', bio='My bio', password='Password123')

        before_count = Post.objects.count()
        post = form.save(user)
        after_count = Post.objects.count()
        self.assertEqual(after_count, before_count+1)
        self.assertEqual(post.author.username, '@janedoe')
        self.assertEqual(post.text, input['text'])
        self.assertEqual(post.user, user)
