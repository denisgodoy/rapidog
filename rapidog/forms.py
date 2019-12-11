from django import forms
from rapidog.models import Newsletter, Usuario

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            'email',
        ]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'sobrenome',
            'email',
        ]