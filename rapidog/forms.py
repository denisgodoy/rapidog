from django import forms
from rapidog.models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            'email',
        ]

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    assunto = forms.CharField(max_length=50)
    mensagem = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(),
        help_text='Digite sua mensagem'
    )
    source = forms.CharField(       
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        assunto = cleaned_data.get('assunto')
        mensagem = cleaned_data.get('mensagem')
        if not nome and not email and not mensagem:
            raise forms.ValidationError('Você precisa escrever uma mensagem.')