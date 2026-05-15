from django import forms
from .models import InternshipPost
class InternshipPostForm(forms.ModelForm):
    class Meta:
        model = InternshipPost
        fields = ['title', 'description', 'required_skills','location','deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'required_skills': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }