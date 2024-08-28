from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password', 'gender']
        widgets = {
            'password': forms.PasswordInput(),
        }
