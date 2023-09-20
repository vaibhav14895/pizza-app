from .models import pizza
from django import forms
class pizza_add(forms.ModelForm):
    
    class Meta:
        model = pizza
        fields = ("__all__")
