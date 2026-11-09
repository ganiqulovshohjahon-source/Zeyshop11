from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactPageTests(TestCase):
    def test_contact_page_displays_form(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="name"')

    def test_valid_contact_submission_is_saved(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Test Customer",
                "email": "customer@example.com",
                "subject": "Product question",
                "message": "Could you share more details?",
            },
        )

        self.assertRedirects(response, reverse("contact"))
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.get().email, "customer@example.com")

    def test_invalid_contact_submission_is_not_saved(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Test Customer",
                "email": "invalid-email",
                "subject": "",
                "message": "A question",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(ContactMessage.objects.count(), 0)
