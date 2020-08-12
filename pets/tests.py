from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pets.views import (
    gallery,
    pet_desc,
    pets,
)

# Create your tests here.

class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_gallery_page(self):
        url = reverse('gallery')
        self.assertEquals(resolve(url).func, gallery)

    def test_pet_desc_page(self):
        url = reverse('pet_desc',args=[1])
        self.assertEquals(resolve(url).func, pet_desc)

    def test_pets(self):
        url = reverse('pets')
        self.assertEquals(resolve(url).func, pets)