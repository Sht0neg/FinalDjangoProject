from django import forms

class CreateVacancyForm(forms.Form):
    title = forms.CharField(max_length=255, label=False,)
    description = forms.CharField(label=False, max_length=255,)
    price = forms.FloatField(label=False, max_value=100000000,)
