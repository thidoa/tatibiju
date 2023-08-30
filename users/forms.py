from django import forms
from .models import Usuario
from django.shortcuts import get_object_or_404

class UserUpdateForm(forms.Form):
    username = forms.CharField(label='Nome', max_length=200, widget=forms.TextInput(attrs={'placeholder':'Nome'}))

    email = forms.EmailField(label='E-mail',  widget=forms.TextInput(attrs={'placeholder':'Ex: tatibiju@tati.biju'}))
    telefone = forms.CharField(required=False, label='Telefone', max_length=11, widget=forms.TextInput(attrs={'placeholder':'(xx)xxxxx-xxxx'}))

    def update_form(self, id):
        usuario = get_object_or_404(Usuario, id=id)

        usuario.username = self.cleaned_data['username']
        usuario.email = self.cleaned_data['email']
        usuario.telefone = self.cleaned_data['telefone']

        usuario.save()

