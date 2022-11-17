from cgi import test
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        # Create a blog post
        test_post = Blog(author=testuser1, title='Blog title',
                         body='Body content...')
        test_post.save()

    def test_blog_content(self):
        post = Blog.objects.get(title='Blog title')
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')
