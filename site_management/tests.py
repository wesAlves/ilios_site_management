"""Testes for site management"""

from django.test import TestCase


class TestSiteManagement(TestCase):
    """Testes for site management"""

    def test_base_one(self) -> None:
        self.assertEqual(1, 1)
