from django import template
from django.urls import reverse
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    return render_menu(menu_items, menu_name)


def render_menu(menu_items, menu_name):
    menu_html = '<ul class="menu">%s</ul>'
    menu_items_html = ''
    for item in menu_items:
        active_class = 'active' if item.url == reverse(menu_name) else ''
        children = item.children.all()
        if children:
            children_html = render_menu(children, menu_name)
            menu_items_html += f'<li class="{active_class}">{item.name}<ul>{children_html}</ul></li>'
        else:
            menu_items_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a></li>'
    return menu_html % menu_items_html
