from django import forms
from account.models import User
from django_select2 import *
from groups.models import GroupUser

class UserChoices(AutoModelSelect2Field):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		res = [(v.id, v.email) for v in User.objects.filter(email__icontains=term).exclude(id=request.user.id)]
		return NO_ERR_RESP, False, res

class AddGroupForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Name"}))

class AddUserToGroupForm(forms.Form):
	user = UserChoices()
	class Meta:
		model = GroupUser	
		fields = ['user']
