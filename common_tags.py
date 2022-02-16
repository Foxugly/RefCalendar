import datetime
import calendar
from django.utils.translation import get_language
from django import template
from django.utils.formats import date_format
from django.utils.translation import gettext as _
register = template.Library()


@register.simple_tag
def get_availability(obj, year, month):
    return obj.get_availability(year, month)


@register.simple_tag
def get_day(day, month, year):
    d = datetime.date(year, month, day)
    return _(calendar.day_name[d.weekday()])[0].capitalize()


@register.simple_tag
def get_month(month):
    return _(calendar.month_name[month]).capitalize()
