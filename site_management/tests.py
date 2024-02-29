"""Testes for site management"""

from django.test import TestCase
from .models import AvailableSite


class TestSiteManagement(TestCase):
    """Testes for site management"""

    @classmethod
    def setUpTestData(cls):

        test_sites = {
            "name": "Site test",
            "desctiption": "This a test site and should be temporary",
            "domain": "example.com",
            "atrributes": "none",
            "theme": "none.theme",
            "base_template": "template one",
            "author": "Wes",
        }

        for i in range(10):

            AvailableSite.objects.create(
                name=f"Site test {i}",
                desctiption="This a test site and should be temporary",
                domain="example.com",
                atrributes="none",
                theme="none.theme",
                base_template="template one",
                author="Wes",
            )

    def test_list_all_sites(self):
        sites = AvailableSite.objects.all()
        self.assertEqual(len(sites), 10)

    def test_list_site_by_id(self):
        site = AvailableSite.objects.get(id=3)
        self.assertEqual(site.name, "Site test 2")

    def test_post_a_site(self):
        pass

    def test_update_a_site(self):
        pass

    def test_delete_a_site(self):
        pass


class TestPageManagement(TestCase):
    pass
