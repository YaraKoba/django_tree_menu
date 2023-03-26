from django import template
from tree_menu.models import *

register = template.Library()


@register.inclusion_tag('tree_menu/nav_bar.html')
def draw_menu(menu, request):
    menu_items = MenuItem.objects.filter(group__name=menu)
    dict_children = render_menu_items(menu_items, request.path)

    return {'item': dict_children, 'menu': menu}


def render_menu_items(menu_items, path):
    menu_tree = []

    # Create a dictionary to store the menu items by name
    menu_dict = {}

    # First pass: create menu items and store them in menu_dict
    for item in menu_items:
        name = item.text
        url = item.slug
        parent = item.parent
        menu_item = {
                    'name': name,
                    'url': url,
                    'is_active': False,
                    'href': item.get_url(),
                    'current': False,
                    'children': [],
                     }

        if path == menu_item['href']:
            menu_item['current'] = True
            menu_item['is_active'] = True

        menu_dict[name] = menu_item
        if parent is None:
            menu_tree.append(menu_item)

    # Second pass: link child items to their parents
    for item in menu_items:
        name = item.text
        if item.parent:
            parent = item.parent
        else:
            parent = None
        if parent is not None:
            parent_item = menu_dict[parent.text]
            if menu_dict[name]['is_active']:

                while parent:
                    menu_dict[parent.text]['is_active'] = True
                    parent = parent.parent

            parent_item['children'].append(menu_dict[name])

    return menu_tree
