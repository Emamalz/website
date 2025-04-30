from django import forms
from .models import Team, HealthCheckEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SelectTeamForm(forms.Form):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        empty_label="Select a Team",
        widget=forms.Select(attrs={'class': 'team-input'})
    )

class HealthCheckEntryForm(forms.ModelForm):
    class Meta:
        model = HealthCheckEntry
        fields = ['card_title', 'status', 'comments', 'actions', 'solutions']




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model  = User
        fields = ("username", "email", "password1", "password2")
