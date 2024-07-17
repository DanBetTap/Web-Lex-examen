from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['rut', 'nombre', 'email']
