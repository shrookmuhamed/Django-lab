from django import forms
from .models import book

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        # fields = ['name', 'image', 'price', 'pages']
        fields = '__all__'
