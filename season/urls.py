from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import SeasonListView, SeasonCreateView, SeasonUpdateView, SeasonDeleteView, SeasonDetailView

app_name = 'season'
urlpatterns = [
    path('season/', login_required(SeasonListView.as_view()), name='season_list'),
    path('season/add/', login_required(SeasonCreateView.as_view()), name="season_add"),
    path('season/<int:pk>/', login_required(SeasonDetailView.as_view()), name="season_detail"),
    path('season/<int:pk>/change/', login_required(SeasonUpdateView.as_view()), name="season_change"),
    path('season/<int:pk>/delete/', login_required(SeasonDeleteView.as_view()), name="season_delete"),
]
