from django.test import TestCase

from .models import shop


class AddProductTests(TestCase):
    def test_add_product_form_is_displayed(self):
        response = self.client.get("/add_product/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form method="post"', html=False)

    def test_add_product_is_saved(self):
        response = self.client.post(
            "/add_product/",
            {"name": "Coffee", "price": 12000, "category": "Drinks"},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/shop/")
        self.assertContains(response, "Coffee")
        self.assertContains(response, "Drinks")
        self.assertContains(response, "12000")
        self.assertTrue(
            shop.objects.filter(
                name="Coffee",
                price=12000,
                category="Drinks",
            ).exists()
        )

    def test_invalid_product_form_is_redisplayed(self):
        response = self.client.post(
            "/add_product/",
            {"name": "Coffee", "price": "not-a-number", "category": "Drinks"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a whole number.")
