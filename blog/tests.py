from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    comments,
    new_comment,
)

# Create your tests here.

class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_all_comments_page(self):
        url = reverse('comments')
        self.assertEquals(resolve(url).func, comments)

    def test_new_comment_page(self):
        url = reverse('new_comment')
        self.assertEquals(resolve(url).func, new_comment)

