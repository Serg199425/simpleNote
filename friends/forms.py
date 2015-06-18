from django import forms
from IPython import embed
from account.models import Friendship, User
from django_select2 import AutoModelSelect2Field, AutoHeavySelect2Widget, NO_ERR_RESP
import operator
from django.db.models import Q

class UserChoices(AutoModelSelect2Field):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		try:
			query_email = reduce(operator.or_, (Q(email__icontains = word) for word in term.split()))
			query_first_name = reduce(operator.or_, (Q(account__first_name__icontains = word) for word in term.split()))
			query_last_name = reduce(operator.or_, (Q(account__last_name__icontains = word) for word in term.split()))
			black_list_ids = list(request.user.account.all_friends().values_list('from_friend_id', flat=True))
			black_list_ids.append(request.user.id)
			results = User.objects.filter(query_first_name | query_last_name | query_email).exclude(id__in=black_list_ids)[:5]
			results = [(u.id, u.email + ' ' + u.account.first_name + ' ' + u.account.last_name) for u in results]
			return NO_ERR_RESP, False, results
		except:
			results = []
			return NO_ERR_RESP, False, results

class AddFriendForm(forms.ModelForm):
	friend = UserChoices(widget=AutoHeavySelect2Widget(
		select2_options = { 'minimumInputLength': 1, 'placeholder':'Add Friend' }))
	class Meta:
		model = Friendship	
		fields = ['friend']
