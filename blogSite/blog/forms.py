from django import forms
from .models import  Article


class ADForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ('title','content')
