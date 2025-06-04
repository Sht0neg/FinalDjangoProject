from django import forms

class ProfileRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, label="Введите своё имя", )
    surname = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    phone = forms.CharField(widget=forms.TelInput)
    password = forms.CharField(widget=forms.PasswordInput)

    role = forms.ChoiceField(choices={"EMP" : "Работодатель", "APP" : "Соискатель"})
    
