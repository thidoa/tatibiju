from django import forms
from products.models import Product

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"