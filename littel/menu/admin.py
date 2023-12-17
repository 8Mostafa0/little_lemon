from django.contrib import admin
from menu.models import Menu_i

class Menu_Item(admin.ModelAdmin):
    pass

admin.site.register(Menu_i,Menu_Item)