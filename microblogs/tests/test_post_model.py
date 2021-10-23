"""Unit tests of the Post model."""
from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import Post, User
from django.utils import timezone

class PostModelTest(TestCase):
    """Unit tests of the Post model."""

    def setUp(self):
        self.user = User.objects.create_user(
        '@johndoe',
        first_name='John',
        last_name='Doe',
        email='johndoe@example.org',
        password='Password123',
        bio='The quick brown fox jumped over the lazy dog'
        )

        self.post = Post.objects.create(
            author = self.user,
            text="I am looking up at the sky"
        )

    def test_valid_post(self):
        self._assert_post_is_valid()

    def test_user_author_be_blank(self):
        self.post.author = None
        self._assert_post_is_invalid()

    def test_date_cannot_be_in_future(self):
        assert self.post.created_at <= timezone.now()

    def test_text_can_be_280_characters_long(self):
        self.post.text = 'x' * 280

    def test_text_cannot_be_nore_than_280_characters_long(self):
        self.post.text = 'x' * 281

    def _assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except (ValidationError):
            self.fail('Test post should be valid')

    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()
