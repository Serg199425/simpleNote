from django import forms
from account.models import User
from django_select2 import *
from groups.models import GroupUser, Group
import operator
from django.db.models import Q

class UserChoices(AutoModelSelect2MultipleField):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		try:
			query_email = reduce(operator.or_, (Q(email__icontains = word) for word in term.split()))
			query_first_name = reduce(operator.or_, (Q(account__first_name__icontains = word) for word in term.split()))
			query_last_name = reduce(operator.or_, (Q(account__last_name__icontains = word) for word in term.split()))
			results = User.objects.filter(query_first_name | query_last_name | query_email).exclude(id=request.user.id)[:5]
			results = [(u.id, u.email + ' ' + u.account.first_name + ' ' + u.account.last_name) for u in results]
			return NO_ERR_RESP, False, results
		except:
			results = []
			return NO_ERR_RESP, False, results

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
