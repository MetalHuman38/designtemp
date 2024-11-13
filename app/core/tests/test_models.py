"""
This module contains tests
for the models of the core app.
"""
from django.test import TestCase
from django.utils import timezone
from uidir import models
from django.core.exceptions import ValidationError


def create_sample_consultation(**kwargs):
    """
    Create a sample consultation.
    """

    defaults = {
        "fullname": "Consultation Client",
        "email": "client@example.com",
        "requirements": "Consultation requirements",
    }
    defaults.update(kwargs)
    return models.Consultation.objects.create(**defaults)


class ConsultationModelTests(TestCase):
    """
    Test the Consultation model.
    """

    def test_consultation_str(self):
        """
        Test the string
        representation of a consultation.
        """

        consultation = create_sample_consultation()
        self.assertEqual(str(consultation), consultation.fullname)

    def test_submit_consultation(self):
        """
        Test submitting a
        consultation with default values.
        """

        consultation = create_sample_consultation()
        self.assertEqual(consultation.fullname, "Consultation Client")
        self.assertEqual(consultation.email, "client@example.com")
        self.assertEqual(consultation.requirements, "Consultation requirements")
        self.assertTrue(consultation.submitted_at)

    def test_missing_required_fields(self):
        """
        Test that missing required
        fields raise an error.
        """

        with self.assertRaises(ValidationError):
            empty_fullname = models.Consultation(
              fullname="", email="client@example.com",
              requirements="Some requirements"
              )
            empty_fullname.full_clean()  # This triggers field validation

        with self.assertRaises(ValidationError):
            empty_email = models.Consultation(
              fullname="Valid Name", email="",
              requirements="Some requirements")
            empty_email.full_clean()

        with self.assertRaises(ValidationError):
            empty_requirements = models.Consultation(
              fullname="Valid Name",
              email="client@example.com",
              requirements="")
            empty_requirements.full_clean()

    def test_email_field_validation(self):
        """
        Test that an invalid email format
        raises a validation error.
        """

        with self.assertRaises(ValidationError):
            invalid_email = models.Consultation(
              fullname="Valid Name",
              email="not-an-email",
              requirements="Some requirements")
            invalid_email.full_clean()

    def test_max_length_fullname(self):
        """
        Test that fullname respects
        the maximum length constraint.
        """

        too_long_name = "A" * 101
        with self.assertRaises(ValidationError):
            long_fullname = models.Consultation(
              fullname=too_long_name,
              email="client@example.com",
              requirements="Some requirements")
            long_fullname.full_clean()

    def test_submitted_at_auto_now_add(self):
        """
        Test that submitted_at is automatically
        set to the current time if not provided.
        """

        consultation = create_sample_consultation()
        self.assertIsNotNone(consultation.submitted_at)
        self.assertAlmostEqual(consultation.submitted_at, timezone.now(), delta=timezone.timedelta(seconds=1))
