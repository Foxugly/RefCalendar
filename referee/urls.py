from .views import RefereeListView, RefereeCreateView, RefereeUpdateView, RefereeDeleteView, RefereeDetailView
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'referee'
urlpatterns = [
    path('referee/', login_required(RefereeListView.as_view()), name='referee_list'),
    path('referee/add/', login_required(RefereeCreateView.as_view()), name="referee_add"),
    path('referee/<int:pk>/', login_required(RefereeDetailView.as_view()), name="referee_detail"),
    path('referee/<int:pk>/change/', login_required(RefereeUpdateView.as_view()), name="referee_change"),
    path('referee/<int:pk>/delete/', login_required(RefereeDeleteView.as_view()), name="referee_delete"),
]
