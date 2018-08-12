from django import forms

from .models import UserRegistration

class UserRegistrationCreateForm(forms.ModelForm):
	class Meta:
		model = UserRegistration
		fields = [
		'name',
		'company',
		'email',	
		]