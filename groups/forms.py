from django import forms
from account.models import User
from django_select2 import AutoHeavySelect2MultipleWidget, AutoModelSelect2MultipleField
from groups.models import GroupUser, Group
from account.forms import UserChoices
from django_select2 import AutoModelSelect2MultipleField, AutoHeavySelect2MultipleWidget

class AddGroupForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Name"}))
	users = UserChoices()
	class Meta:
		model = Group	
		fields = ['name']

class AddUserToGroupForm(forms.ModelForm):
	users = UserChoices(required=False, widget=AutoHeavySelect2MultipleWidget(
		select2_options = { 'minimumInputLength': 1, 'placeholder':'Add Users' }))
	class Meta:
		model = Group
		fields = ['users']
