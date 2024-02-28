"""site_management URL Configuration"""

from django.urls import path

from . import views

app_name = "site_management"

urlpatterns = [path("", views.SiteManagementView.as_view(), name="index")]
