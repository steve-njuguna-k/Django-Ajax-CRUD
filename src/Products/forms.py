from .models import Products
from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'category', 'quantity', 'price')