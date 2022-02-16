from django import forms
from django.contrib.auth.models import User

from .models import Referee


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields["is_active"].help_text = None
        self.fields["is_active"].widget.attrs['class'] = 'form-control'


class UpdateAdminUserForm(UpdateUserForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields["is_active"].help_text = None
        self.fields["is_staff"].help_text = None
        self.fields["is_superuser"].help_text = None


class UpdateRefereeForm(forms.ModelForm):
    event_text = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Referee
        fields = ['language', 'color', 'event_text']

    def __init__(self, *args, **kwargs):
        super(UpdateRefereeForm, self).__init__(*args, **kwargs)
        self.fields["language"].widget.attrs['class'] = 'form-control'
        self.fields["color"].widget.attrs['class'] = 'form-control'
