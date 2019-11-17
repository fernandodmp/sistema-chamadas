from django import forms
from .models import Course


class SubscribeForm(forms.Form):
    course_key = forms.CharField(label="Chave de Acesso", max_length=12, widget=forms.TextInput(
        attrs={'placeholder': "Chave de acesso ao curso", 'class': "form-control"}))


class CheckInForm(forms.Form):
    auth_code = forms.CharField(max_length=6, widget=forms.TextInput(
        attrs={'placeholder': "Código de autenticação", 'class': "form-control"}))


class CourseCreation(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'description', 'access_key']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'access_key': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': "Nome",
            'description': "Descrição",
            'access_key': "Chave de Acesso",
        }
