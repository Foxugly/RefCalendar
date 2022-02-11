from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from season.models import Season


# Create your models here.
class Event(models.Model):
    start = models.DateField(blank=False, null=False, verbose_name=_("StarDate"))
    end = models.DateField(blank=False, null=False, verbose_name=_("EndDate"))
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, null=True, blank=True, on_delete=models.CASCADE)

    def start_t(self):
        return self.start.strftime('%Y-%m-%d')

    def end_t(self):
        return self.end.strftime('%Y-%m-%d')

    def as_json(self, **kwargs):
        d = {'id': str(self.id), 'start': self.start_t(), 'end': self.end_t()}
        for k, v in kwargs.items():
            d[k] = v
        return d

    def __str__(self):
        return f"[{self.id}] {self.user.first_name} {self.user.last_name}: {self.start}-{self.end}"
