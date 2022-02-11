from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Season(models.Model):
    name = models.CharField(max_length=64, blank=False, verbose_name=_("Name"), default="season")
    start = models.DateField(blank=False, null=False, verbose_name=_("StarDate"), default=timezone.now)
    end = models.DateField(blank=False, null=False, verbose_name=_("EndDate"), default=timezone.now)
    active = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        self.app_name = "season"
        self.model_name = "season"
        self.change_url = '%s:%s_change' % (self.app_name, self.model_name)
        self.add_url = '%s:%s_add' % (self.app_name, self.model_name)
        self.detail_url = '%s:%s_detail' % (self.app_name, self.model_name)
        self.delete_url = '%s:%s_delete' % (self.app_name, self.model_name)
        self.list_url = '%s:%s_list' % (self.app_name, self.model_name)
        self.verbose_name = _("Seasons")
        super(Season, self).__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

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
