from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import Feedback
from .models import *
from django.contrib.auth.forms import UserCreationForm

#from .models import Comment, Post 



# Default form for this app


class HomeForm(forms.Form):

	# text input field for this form
	post = forms.CharField()
	#against = forms.CharField()
    
class HomeForm2(forms.Form):

	# text input field for this form
    post=forms.CharField()
    against = forms.CharField()

class DNAForm(forms.ModelForm):

    # Text fields for name and sequence input
    name = forms.CharField()
    sequence = forms.CharField()

    # Set metadata for this form so that it can update models
    class Meta:
        model = DNASeq
        fields = ('name', 'sequence',)


# Form for RNA sequence upload

class RNAForm(forms.ModelForm):

    # Text fields for name and sequence input
    name = forms.CharField()
    sequence = forms.CharField()

    # Set metadata for this form so that it can update models
    class Meta:
        model = RNASeq
        fields = ('name', 'sequence',)


# Form for peptide sequence upload

class PeptideForm(forms.ModelForm):

    # Text fields for name and sequence input
    name = forms.CharField()
    sequence = forms.CharField()

    # Set metadata for this form so that it can update models
    class Meta:
        model = PeptideSeq
        fields = ('name', 'sequence',)


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']