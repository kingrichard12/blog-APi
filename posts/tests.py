from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",

        )
        cls.post=Post.objects.create(
            author=cls.user,
            title="A good title",
            body="nice body content",

        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "nice body content")
        self.assertEqual(str(self.post), "A good title")
