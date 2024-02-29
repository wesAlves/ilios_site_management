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

    def __str__(self):
        return f"{self.name} - {self.domain}"


class Page(models.Model):
    name = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200, blank=True)
    viewport = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    templates = models.CharField(max_length=200, blank=True)
    domain = models.ForeignKey("AvailableSite", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.domain} - {self.name}"


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
    aria = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Container(models.Model):
    name = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    variant = models.CharField(max_length=200, blank=True)
    attribute = models.CharField(max_length=200, blank=True)
    content = models.CharField(max_length=200, blank=True)
    aria = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    css_classes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Theme(models.Model):
    name = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=200, blank=True)
    logo = models.CharField(max_length=200, blank=True)
    graphisms = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Template(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"
