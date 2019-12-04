from django import forms
from rapidog.models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            'email',
        ]