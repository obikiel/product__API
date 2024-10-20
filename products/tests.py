from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product")

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")

# Create your tests here.
