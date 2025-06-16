from django import forms
from  django.core.validators import RegexValidator

class ProfileRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, label=False, )
    surname = forms.CharField(max_length=100, label=False,)
    last_name = forms.CharField(max_length=100, label=False,)

    phone = forms.CharField(widget=forms.TelInput, label=False, validators=[RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$', message="Вы ввели неверный номер телефона", code="errorphone"),], error_messages={"errorphone": "Please enter your phone"})
    password = forms.CharField(widget=forms.PasswordInput, label=False,)

    role = forms.ChoiceField(choices={"EMP" : "Работодатель", "APP" : "Соискатель"}, label=False,)

class ProfileLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TelInput, label=False, validators=[RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$', message="Вы ввели неверный номер телефона", code="errorphone"),], error_messages={"errorphone": "Please enter your phone"})
    password = forms.CharField(widget=forms.PasswordInput, label=False,)
    
