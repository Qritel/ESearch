from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Champs obligatoires. veuillez saisir une adresse email valide.')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Votre mot de passe doit contenir au minimum 8 caractères. Et ne peut pas être entièrement numérique.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
