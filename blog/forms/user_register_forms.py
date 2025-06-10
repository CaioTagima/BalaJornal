from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from blog.models.user import User

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'username': 'Nome de Usuário',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'E-mail': 'seu@email.com'}),
            'username': forms.TextInput(attrs={'placeholder': 'George e Matheus'}),
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username) < 3:  
            raise ValidationError("O nome de usuário deve ter pelo menos 3 caracteres.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está cadastrado.")
        return email
