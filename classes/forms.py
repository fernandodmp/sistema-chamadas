from django import forms


class SubscribeForm(forms.Form):
    course_key = forms.CharField(max_length=12)


class CheckInForm(forms.Form):
    course_key = forms.CharField(max_length=6)
