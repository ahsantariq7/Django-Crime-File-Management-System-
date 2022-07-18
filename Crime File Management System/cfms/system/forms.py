from django import forms
from .models import AddMissingPerson
from .models import ShowMostWantedPerson

class AddMissingPersonForm(forms.ModelForm):

    class Meta:
        model = AddMissingPerson
        fields = ["title", "cover"]

class ShowMostWantedPersonForm(forms.ModelForm):

    class Meta:
        model = ShowMostWantedPerson
        fields = ["title", "cover"]

