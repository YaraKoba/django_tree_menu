from django.contrib import admin
from tree_menu.models import MenuGroup, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'group', 'parent', 'get_children')


admin.site.register(MenuItem, MenuItemAdmin)

admin.site.register(MenuGroup)

