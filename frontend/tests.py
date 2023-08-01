from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from .models import Customer_contact_info

class ContactUsViewTest(TestCase):
    def test_contact_us_view(self):
        url = reverse('contact_us')
        response = self.client.get(url)

        # Assert that the view returns a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used for rendering
        self.assertTemplateUsed(response, 'index.html')

        # Assert that the view is using the correct form
        self.assertIsInstance(response.context['contact_form'], ContactForm)

    def test_post_contact_us_view(self):
        url = reverse('contact_us')
        data = {
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'customer_contact_subject': 'Test Subject',
            'customer_notes': 'This is a test message.',
        }

        # Send a POST request to the view with form data
        response = self.client.post(url, data)

        # Assert that the view redirects to the 'home' URL after a successful POST
        self.assertRedirects(response, reverse('home'))

        # Assert that the form is valid and saves the data to the database
        self.assertTrue(ContactForm.objects.exists())

    def test_invalid_contact_us_view(self):
        url = reverse('contact_us')
        data = {}  # Empty data, making the form invalid

        # Send a POST request to the view with invalid form data
        response = self.client.post(url, data)

        # Assert that the view redirects to the 'home' URL even with invalid data
        self.assertRedirects(response, reverse('home'))




#model test cases


class CustomerContactInfoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer_contact_info.objects.create(
            customer_name="John Doe",
            customer_email="john@example.com",
            customer_phone="+123456789",
            customer_contact_subject="Website Issue",
            internal_customer_contact_subject="RECEIVED",
            customer_notes="Test message",
            internal_progress="IN PROGRESS",
            work_estimate=100.0,
            payment_complete=False,
        )

    def test_customer_id_generated_correctly(self):
        contact = Customer_contact_info.objects.get(customer_name="John Doe")
        self.assertTrue(contact.customer_id.isupper())
        self.assertEqual(len(contact.customer_id), 16)

    def test_str_representation(self):
        contact = Customer_contact_info.objects.get(customer_name="John Doe")
        self.assertEqual(str(contact), "John Doe")

    def test_submission_time_auto_set(self):
        contact = Customer_contact_info.objects.get(customer_name="John Doe")
        self.assertIsNotNone(contact.submission_time)

    def test_default_payment_complete(self):
        contact = Customer_contact_info.objects.get(customer_name="John Doe")
        self.assertFalse(contact.payment_complete)

    def test_model_verbose_names(self):
        self.assertEqual(
            Customer_contact_info._meta.verbose_name, "Customer Contact"
        )
        self.assertEqual(
            Customer_contact_info._meta.verbose_name_plural, "Customers"
        )

    def test_model_choices(self):
        contact = Customer_contact_info.objects.get(customer_name="John Doe")
        self.assertIn(contact.internal_customer_contact_subject, [choice[0] for choice in contact.CONTACT_SUBJECT_CHOICES])
        self.assertIn(contact.internal_progress, [choice[0] for choice in contact.INTERNAL_PROGRESS])
