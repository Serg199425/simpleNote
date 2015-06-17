from django import forms
from account.models import User
from django_select2 import *
from groups.models import GroupUser, Group

class UserChoices(AutoModelSelect2MultipleField):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		res = [(u.id, u.email) for u in User.objects.filter(email__icontains=term).exclude(id=request.user.id)]
		return NO_ERR_RESP, False, res

class AddGroupForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Name"}))
	users = UserChoices()
	class Meta:
		model = Group	
		fields = ['name']

class AddUserToGroupForm(forms.ModelForm):
	users = UserChoices(required=False, widget=AutoHeavySelect2MultipleWidget(attrs={'placeholder':'Add Users'}))
	class Meta:
		model = Group
		fields = ['users']
