from django.contrib import admin

# Register your models here.

from . models import Document, TableProducts

admin.site.register(Document)
admin.site.register(TableProducts)
