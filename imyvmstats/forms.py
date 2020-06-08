from django import forms
from imyvmstats.models import EcoAccounts

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = EcoAccounts
        fields = ("player","money", )   # NOTE: the trailing comma is required