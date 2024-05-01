from django.contrib import admin

from .models import PoemsModel, PoetsModel, PoetAdmin,PoemAdmin

admin.site.register(PoetsModel, PoetAdmin)
admin.site.register(PoemsModel, PoemAdmin)
