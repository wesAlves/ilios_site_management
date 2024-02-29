"""site_management URL Configuration"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = "site_management"

router = SimpleRouter()
router.register(r"site", views.SiteManagementView, basename="site")
router.register(r"page", views.PageViewSet, basename="page")
router.register(r"section", views.SectionViewSet, basename="section")
router.register(
    r"site-management/container", views.ContainerViewSet, basename="container"
)
# # TODO: that will ne to be moved to another app
# router.register(r"theme", views.Theme, basename="theme")
# router.register(r"template", views.ThemeSerializer, basename="template")

urlpatterns = []

urlpatterns += router.urls
