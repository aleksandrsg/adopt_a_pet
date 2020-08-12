from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import (
   index,
)

# Create your tests here.

class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_index_page(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)