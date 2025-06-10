from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from ..models.user_detail import UserDetail
from django.contrib.auth.models import User

class UserDetailForm(UserCreationForm):
    full_name = forms.CharField(
        label='Nome Completo',
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo'}))
    
    address = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}))
    
    age = forms.IntegerField(
        label='Idade',
        widget=forms.NumberInput(attrs={'min': '18'}))  # Validação mínima
    
    cpf = forms.CharField(
        label='CPF',
        widget=forms.TextInput(attrs={'placeholder': '123.456.789-00'}),
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='Formato inválido (use 123.456.789-00)'
            )
        ])
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserDetail.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                address=self.cleaned_data['address'],
                age=self.cleaned_data['age'],
                cpf=self.cleaned_data['cpf']
            )
        return user
