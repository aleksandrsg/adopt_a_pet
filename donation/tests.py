from django.test import SimpleTestCase
from django.urls import reverse, resolve
from donation.views import (
    donation,
    charge,
    successMsg,
)

# Create your tests here.

class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_donation_page(self):
        url = reverse('donation')
        self.assertEquals(resolve(url).func, donation)

    def test_success_page(self):
        url = reverse('success', args=[1])
        self.assertEquals(resolve(url).func, successMsg)

    def test_charge(self):
        url = reverse('charge')
        self.assertEquals(resolve(url).func, charge)