from django import forms
from django.contrib.auth.models import User
from IPython import embed
from account.models import Friendship
from django_select2 import *

class UserChoices(AutoModelSelect2Field):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		res = [(v.id, v.email) for v in User.objects.filter(email__icontains=term).exclude(id=request.user.id)]
		return NO_ERR_RESP, False, res

class AddFriendForm(forms.ModelForm):
	friend = UserChoices()
	class Meta:
		model = Friendship	
		fields = ['friend']
