"""site_management URL Configuration"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = "site_management"


urlpatterns = [
    path("site/", views.SiteManagementView.as_view(), name="site"),
    path("site/<int:id>/", views.SiteManagementView.as_view(), name="site_by_id"),
    path("page/", views.PageView.as_view(), name="page"),
    path("page/<int:id>/", views.PageView.as_view(), name="page_by_id"),
    path("section/", views.SectionView.as_view(), name="section"),
    path("section/<int:id>/", views.SectionView.as_view(), name="section_by_id"),
    path("container//", views.ContainerView.as_view(), name="container"),
    path("container/<int:id>/", views.ContainerView.as_view(), name="container_by_id"),
]
