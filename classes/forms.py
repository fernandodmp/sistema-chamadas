from django import forms


class SubscribeForm(forms.Form):
    course_key = forms.CharField(label = "Chave de Acesso", max_length=12, widget=forms.TextInput(
        attrs={'placeholder': "Chave de acesso ao curso", 'class': "form-control"}))


class CheckInForm(forms.Form):
    auth_code = forms.CharField(max_length=6, widget=forms.TextInput(
        attrs={'placeholder': "Código de autenticação", 'class': "form-control"}))
