
from django.core.exceptions import ValidationError
from django import forms
from django.forms import widgets
from webapp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'description','balance','price']
    