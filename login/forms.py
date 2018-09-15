from django import forms
from django.contrib.auth.models import User


class LoginRegistrationForm(forms.Form):
    username = forms.RegexField(regex='', widget=forms.TextInput(attrs=dict(require=True, max_length=30)),
                                label='Usuário', error_messages={
            'Invalid': 'Usuário deve conter apenas letras e números!'})

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(require=True, max_length=60)), label='Email')

    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(require=True, max_length=30, render_value=False)),
                               label='Senha')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(require=True, max_length=30, render_value=False)),
                                label='Confirme sua senha')

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError('Esse usuário já existe, informe outro usuário válido!')

    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError('As senhas devem ser iguais, tente novamente!')

        return self.cleaned_data
