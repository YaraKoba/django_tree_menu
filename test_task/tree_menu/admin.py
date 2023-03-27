from django.contrib import admin
from tree_menu.models import MenuGroup, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'group', 'parent', 'get_children')
    prepopulated_fields = {'slug': ("text",)}


class MenuGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(MenuItem, MenuItemAdmin)

admin.site.register(MenuGroup, MenuGroupAdmin)
