from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.utils.translation import activate


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        c = {}
        return render(request, "home.html", c)


@login_required
def dashboard(request):
    activate(request.user.referee.language)
    c = {'event_url': f'/event/json/{request.user.id}'}
    return render(request, "dashboard.html", c)


def set_language(request):
    if request.user.is_authenticated and 'lang' in request.GET and 'next' in request.GET:
        request.user.referee.language = request.GET.get('lang')
        request.user.referee.save()
        next_url = request.GET.get('next')
        if isinstance(next_url, str):
            activate(request.GET.get('lang'))
            return redirect(next_url)
        else:
            return reverse('home')
    elif 'lang' in request.GET:
        activate(request.GET.get('lang'))
    return HttpResponseRedirect(reverse('home'))


@login_required
def report(request):
    c = {'event_url': f'/event/json/{request.user.id}'}
    return render(request, "dashboard.html", c)
