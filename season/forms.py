from django import forms

from .models import Season


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'start', 'end', 'active', 'send_reminder', 'title_email', 'content_email']
        widgets = {
            'start': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'end': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

    def __init__(self, *args, **kwargs):
        super(SeasonForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs['class'] = 'form-control'
        self.fields["title_email"].widget.attrs['class'] = 'form-control'
        self.fields["content_email"].widget.attrs['class'] = 'form-control'
        self.fields["active"].widget.attrs['class'] = 'form-control'
        self.fields["send_reminder"].widget.attrs['class'] = 'form-control'
