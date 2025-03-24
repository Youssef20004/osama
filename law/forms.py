from django import forms
from .models import SumData

class FormSumData(forms.ModelForm): 
    class Meta:
        model = SumData
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
