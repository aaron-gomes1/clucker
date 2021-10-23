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
