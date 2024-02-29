from django.contrib import admin

from .models import AvailableSite, Section, Page, Container

admin.site.register(AvailableSite)
admin.site.register(Page)
admin.site.register(Section)
admin.site.register(Container)
