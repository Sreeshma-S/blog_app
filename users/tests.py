from http import HTTPStatus

from django.test import TestCase
import datetime
from blogapp.models import Post
from django.contrib.auth.models import User

# Create your tests here.

class PostTest(TestCase):
    def test_post_exists(self):
        posts = Post.objects.all().exists()
        self.assertFalse(posts, 0)


    def test_string_representation(self):
        post = Post.objects.create(
            author=User.objects.create_user(username='testuser', password='password'),
            title = 'Test Post',
            text = 'Test Text',
            date = datetime.datetime.now(),
        )

        self.assertEqual(str(post), post.title)

class HomePageTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(
            author=User.objects.create_user(username='testuser32', password='password'),
            title='Sample Post 1',
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            date=datetime.datetime.now(),
        )

        Post.objects.create(
            author=User.objects.create_user(username='testuser65', password='password'),
            title='Sample Post 2',
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            date=datetime.datetime.now(),
        )

    def test_home_page_correct_response(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'users/base.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
