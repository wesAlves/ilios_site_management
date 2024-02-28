"""site_management URL Configuration"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = "site_management"

router = SimpleRouter()
router.register(r"", views.SiteManagementView, basename="site_management")

urlpatterns = []

urlpatterns += router.urls
