from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Atinizdi kiritin'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Parolinizdi kiritin', 'class': 'password'}))



class UserRegistrationForm(UserCreationForm):
    klass = forms.IntegerField(min_value=1, max_value=11)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):

        super(UserRegistrationForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['placeholder'] = 'Atinizdi kiritin'

        self.fields['email'].widget.attrs['placeholder'] = 'Pochtanizdi kiritin'

        self.fields['password1'].widget.attrs['placeholder'] = 'Parolinizdi kiritin'

        self.fields['password2'].widget.attrs['placeholder'] = 'Parolinizdi tasdiqlan'

        self.fields['klass'].widget.attrs['placeholder'] = 'Klassinizdi kiritin'

        self.fields['password1'].widget.attrs['class'] = 'password1'

        self.fields['password2'].widget.attrs['class'] = 'password2'




    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            klass = self.cleaned_data['klass']
            Profile.objects.create(user=user, klass=klass)
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):

        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Atinizdi kiritin'
        self.fields['email'].widget.attrs['placeholder'] = 'Pochtanizdi kiritin'

            

class ProfileEditForm(forms.ModelForm):

    class Meta: 
        model = Profile
        fields = ['photo', 'klass']


    def __init__(self, *args, **kwargs):

        super(ProfileEditForm, self).__init__(*args, **kwargs)


        self.fields['photo'].widget.attrs['class'] = 'photo'

        self.fields['klass'].widget.attrs['class'] = 'klass'



