"""View for managing"""

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class SiteManagementView(View):
    """doc"""

    def get(self, request) -> HttpResponse:
        """
        Renders the view with content
        :return: str
        """
        return HttpResponse("jaca")
