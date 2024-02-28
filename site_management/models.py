from django.db import models


# Create your models here.
class AvailableSite(models.Model):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    atrributes = models.CharField(max_length=200, blank=True)
    theme = models.CharField(max_length=200, blank=True)
    base_template = models.CharField(max_length=200, blank=True)
    desctiption = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)


class Page(models.Model):
    name = models.CharField(max_length=200)
    site: models.ForeignKey(
        "AvailableSite", on_delete=models.CASCADE, null=True, blank=True
    )
    keywords = models.CharField(max_length=200, blank=True)
    viewport = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    body = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    templates = models.CharField(max_length=200, blank=True)


class Section(models.Model):
    name = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    css_classes = models.CharField(max_length=200, blank=True)
    pages = models.ManyToManyField(
        "Page", related_name="sections_page", null=True, blank=True
    )
    children = models.ManyToManyField(
        "Container", related_name="sections_children", null=True, blank=True
    )


class Container(models.Model):
    name = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    variant = models.CharField(max_length=200, blank=True)
    attribute = models.CharField(max_length=200, blank=True)
    content = models.CharField(max_length=200, blank=True)
    aria = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)


class Theme(models.Model):
    name = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=200, blank=True)
    logo = models.CharField(max_length=200, blank=True)
    graphisms = models.CharField(max_length=200, blank=True)


class Template(models.Model):
    name = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=200, blank=True)
    logo = models.CharField(max_length=200, blank=True)
    graphisms = models.CharField(max_length=200, blank=True)
