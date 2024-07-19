# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormSpanish(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Las contraseñas no coinciden.',
        'username_taken': 'Este nombre de usuario ya está en uso.',
        'password_too_similar': 'La contraseña no puede ser demasiado similar a tu información personal.',
        'password_common': 'La contraseña no puede ser una contraseña comúnmente utilizada.',
        'password_numeric': 'La contraseña no puede ser completamente numérica.',
    }

    username = forms.CharField(label='Nombre de usuario', max_length=150, help_text='Requerido. 150 caracteres como máximo. Letras, dígitos y @/./+/-/_ solamente.')
    password1 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput, help_text='Tu contraseña no puede ser demasiado similar a tu información personal.')
    password2 = forms.CharField(label='Confirmar contraseña', strip=False, widget=forms.PasswordInput, help_text='Ingresa la misma contraseña que antes, para verificar.')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
