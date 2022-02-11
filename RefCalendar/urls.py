"""RefCalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from event.views import get_event_url, event_add, event_remove
from referee.views import ReportView, ProfileUpdateView
from .views import home, dashboard, set_language

urlpatterns = [
    path('', home, name='home'),
    path('event/json/<int:user_id>', get_event_url, name="get_event_json"),
    path('event/add/', event_add, name="add_event"),
    path('event/delete/', event_remove, name="delete_event"),
    path('dashboard/', dashboard, name="dashboard"),
    path('report/', ReportView.as_view(), name="report"),
    path('lang/', set_language, name='lang'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('referee/', include('referee.urls')),
    path('season/', include('season.urls')),
    path('profile/', ProfileUpdateView.as_view(), name="profile"),
    path('admin/', admin.site.urls),
]
