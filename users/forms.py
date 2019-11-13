from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Person


class PersonCreationForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email')


class PersonChangeForm(UserChangeForm):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email')
