from django import forms
from .models import GuestbookEntry

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['author_name', 'author_email', 'text']
        labels = {
            'author': 'Имя',
            'email': 'Email',
            'text': 'Текст',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите текст записи'}),
        }

class SearchForm(forms.Form):
    search = forms.CharField(required=False, label="Поиск")