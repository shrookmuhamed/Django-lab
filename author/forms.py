from django import forms
from .models import author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = author
        # fields = ['name', 'image', 'price', 'pages']
        fields = '__all__'