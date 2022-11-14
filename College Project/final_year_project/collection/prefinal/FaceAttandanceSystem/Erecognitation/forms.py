from django import forms

class usernameForm(forms.Form):
	username=forms.CharField(max_length=30)