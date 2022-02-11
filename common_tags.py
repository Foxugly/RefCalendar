from django import template

register = template.Library()


@register.simple_tag
def get_availability(obj, year, month):
    return obj.get_availability(year, month)
