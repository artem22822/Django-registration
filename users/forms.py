from django import forms

from django import forms

class ProductSearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Search products...'}))