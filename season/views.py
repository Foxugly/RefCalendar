from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .forms import SeasonForm
from .models import Season


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class SeasonListView(ListView):
    model = None
    paginate_by = 20
    ordering = ['pk']
    template_name = 'season_list.html'

    def __init__(self, *args, **kwargs):
        super(SeasonListView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SeasonListView, self).get_context_data(**kwargs)
        context['model'] = Season
        context['title'] = _("List of Season")
        return context

    def get_queryset(self):
        return Season.objects.all().order_by("-pk")


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class SeasonCreateView(SuccessMessageMixin, CreateView):
    def __init__(self, *args, **kwargs):
        self.model = Season
        self.app_name = "season"
        self.model_name = "season"
        self.form_class = SeasonForm
        self.template_name = 'season_update.html'
        self.success_message = _('season created')
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        super(SeasonCreateView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SeasonCreateView, self).get_context_data(**kwargs)
        context['model'] = self.model
        context['title'] = _("Add Season")
        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class SeasonUpdateView(SuccessMessageMixin, UpdateView):
    def __init__(self, *args, **kwargs):
        self.model = Season
        self.app_name = "season"
        self.model_name = "season"
        self.template_name = 'season_update.html'
        self.success_message = _('season updated')
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        self.form_class = SeasonForm
        super(SeasonUpdateView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SeasonUpdateView, self).get_context_data(**kwargs)
        context['model'] = self.model
        context['title'] = _("Update Season")
        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class SeasonDetailView(DetailView):
    def __init__(self, *args, **kwargs):
        self.model = Season
        self.app_name = "season"
        self.model_name = "season"
        self.fields = "__all__"
        self.template_name = 'season_detail.html'
        self.success_message = None
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        super(SeasonDetailView, self).__init__(*args, **kwargs)


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class SeasonDeleteView(SuccessMessageMixin, DeleteView):

    def __init__(self, *args, **kwargs):
        self.model = Season
        self.app_name = "season"
        self.model_name = "season"
        self.template_name = 'season_confirm_delete.html'
        self.success_message = _('Season deleted.')
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        super(SeasonDeleteView, self).__init__(*args, **kwargs)

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(SeasonDeleteView, self).get_context_data(**kwargs)
        context['model'] = self.model
        context['title'] = _("Delete Season")
        return context
