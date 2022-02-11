from calendar import monthrange
from datetime import date

from colorfield.fields import ColorField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from event.models import Event


# Create your models here.
class Referee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(_("language"), max_length=8, choices=settings.LANGUAGES, default=1)
    events = models.ManyToManyField(Event, blank=True, related_name=_("events"))
    color = ColorField(default='#FF0000')
    event_text = models.CharField(_("text"), max_length=64, default="Unavailable")

    def __init__(self, *args, **kwargs):
        self.app_name = "referee"
        self.model_name = "referee"
        self.change_url = '%s:%s_change' % (self.app_name, self.model_name)
        self.add_url = '%s:%s_add' % (self.app_name, self.model_name)
        self.detail_url = '%s:%s_detail' % (self.app_name, self.model_name)
        self.delete_url = '%s:%s_delete' % (self.app_name, self.model_name)
        self.list_url = '%s:%s_list' % (self.app_name, self.model_name)
        self.verbose_name = _("Referee's")
        super(Referee, self).__init__(*args, **kwargs)

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_edit_url(self):
        return reverse(self.change_url, kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse(self.change_url, kwargs={'pk': self.pk})

    def get_add_url(self):
        return reverse(self.add_url)

    def get_absolute_url(self):
        return reverse(self.detail_url, kwargs={'pk': self.pk})

    def get_full_url(self):
        return "%s%s" % (settings.WEBSITE, self.get_absolute_url())

    def get_detail_url(self):
        return reverse(self.detail_url, kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse(self.delete_url, kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse(self.list_url)

    def get_events(self):
        return self.events.all()

    def get_availability(self, year, month):
        num_days = monthrange(year, month)[1]
        list_out = []
        for day in range(1, num_days + 1):
            date_day = date(year, month, day)
            e = self.events.filter(start__lte=date_day, end__gt=date_day)
            list_out.append(0 if e else 1)
        return list_out
