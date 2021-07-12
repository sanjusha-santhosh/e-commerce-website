from django import forms
from .models import Regi,productlist,cartlist

class UserForm(forms.ModelForm):
    class Meta:
        model=Regi
        fields = "__all__"

class productForm(forms.ModelForm):
    class Meta:
        model=productlist
        fields = "__all__"

class cartForm(forms.ModelForm):
    class Meta:
        model=cartlist
        fields = "__all__"
