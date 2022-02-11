from calendar import monthrange
from datetime import date

import numpy as np
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .forms import UpdateUserForm, UpdateAdminUserForm, UpdateRefereeForm
from .models import Referee


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    def __init__(self, *args, **kwargs):
        self.model = User
        self.template_name = 'profile.html'
        self.success_message = _('Your profile is updated successfully')
        self.success_url = reverse_lazy('profile')
        self.form_class = UpdateUserForm
        self.referee_form_class = UpdateRefereeForm
        super(ProfileUpdateView, self).__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        referee_form = self.referee_form_class(instance=request.user.referee)
        c = {'form': form, 'referee_form': referee_form, }
        return render(request, self.template_name, c)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        referee_form = self.referee_form_class(request.POST, instance=request.user.referee)
        if form.is_valid() and referee_form.is_valid():
            form.save()
            referee_form.save()
            messages.success(request, self.success_message)
            return redirect(to='profile')
        else:
            c = {'form': form, 'referee_form': referee_form, }
            return render(request, self.template_name, c)

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=self.kwargs['pk'])
        # return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class RefereeListView(ListView):
    model = None
    paginate_by = 20
    ordering = ['pk']
    template_name = 'referee_list.html'

    def __init__(self, *args, **kwargs):
        super(RefereeListView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RefereeListView, self).get_context_data(**kwargs)
        context['model'] = Referee
        return context

    def get_queryset(self):
        refs = Referee.objects.all().order_by("user__last_name")
        return refs


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class RefereeCreateView(SuccessMessageMixin, CreateView):
    def __init__(self, *args, **kwargs):
        self.model = User
        self.app_name = "referee"
        self.model_name = "referee"
        self.form_class = UpdateUserForm
        self.template_name = 'referee_update.html'
        self.success_message = _('referee created')
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        super(RefereeCreateView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RefereeCreateView, self).get_context_data(**kwargs)
        context['model'] = self.model
        context['title'] = _("Add Referee")
        return context

    def form_valid(self, form):
        response = super(RefereeCreateView, self).form_valid(form)
        r = Referee(user=self.object)
        r.save()
        return response


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class RefereeUpdateView(SuccessMessageMixin, UpdateView):
    def __init__(self, *args, **kwargs):
        self.model = User
        self.app_name = "referee"
        self.model_name = "referee"
        self.template_name = 'referee_update.html'
        self.success_message = _('referee updated')
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        self.form_class = UpdateAdminUserForm
        super(RefereeUpdateView, self).__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RefereeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RefereeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=self.kwargs['pk'])
        # return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(RefereeUpdateView, self).get_context_data(**kwargs)
        context['model'] = self.model
        context['title'] = _("Update Referee")
        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class RefereeDetailView(DetailView):
    def __init__(self, *args, **kwargs):
        self.model = Referee
        self.app_name = "referee"
        self.model_name = "referee"
        self.fields = "__all__"
        self.template_name = 'referee_detail.html'
        self.success_message = None
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        super(RefereeDetailView, self).__init__(*args, **kwargs)


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class RefereeDeleteView(SuccessMessageMixin, DeleteView):

    def __init__(self, *args, **kwargs):
        self.model = Referee
        self.app_name = "referee"
        self.model_name = "referee"
        self.success_message = _('object deleted.')
        self.success_url = reverse_lazy('%s:%s_list' % (self.app_name, self.model_name))
        super(RefereeDeleteView, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return self.success_url


@method_decorator([login_required, user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('home'))],
                  name="dispatch")
class ReportView(ListView):
    model = None
    paginate_by = 20
    ordering = ['pk']
    template_name = 'report_list.html'

    def __init__(self, *args, **kwargs):
        super(ReportView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        m: int = int(self.request.GET["month"]) if "month" in self.request.GET else 2
        year: int = int(self.request.GET["year"]) if "year" in self.request.GET else 2022
        context['next_m'] = m + 1 if m < 11 else 1
        context['next_y'] = year + 1 if m == 12 else year
        context['prev_m'] = m - 1 if m > 1 else 12
        context['prev_y'] = year - 1 if m == 1 else year
        context['model'] = Referee
        context['year'] = year
        context['month'] = m
        context['month_str'] = date(year, m, 1).strftime('%B')
        n_days = monthrange(year, m)[1]
        context['days'] = range(1, n_days + 1)
        total = [0 * n_days]
        for r in self.get_queryset():
            total += np.array(r.get_availability(year, m))
        context['total_days'] = total
        return context

    def get_queryset(self):
        return Referee.objects.filter(user__is_active=True).order_by("user__last_name")

    def get(self, request, *args, **kwargs):
        return super(ReportView, self).get(request, *args, **kwargs)
