from django import forms
from .models import Team, HealthCheckEntry

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
