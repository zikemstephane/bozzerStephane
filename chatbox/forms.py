# forms.py
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Écrivez votre message ici...'}),
        }
