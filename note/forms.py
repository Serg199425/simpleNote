from django import forms
from redactor.widgets import RedactorEditor
from redactor.fields import RedactorField
from note.models import Note, NoteGroup
from groups.models import Group
from django_select2 import *
from account.models import User
from IPython import embed
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

class GroupChoices(AutoModelSelect2MultipleField):
	queryset = Group.objects
	search_fields = ['name__icontains', ]
	def get_results(self, request, term, page, context):
		res = [(g.id, g.name) for g in request.user.group_set.all().filter(name__icontains=term)]
		return NO_ERR_RESP, False, res

class EditNoteForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Title"}))
	groups = GroupChoices(required=False, widget=AutoHeavySelect2MultipleWidget(attrs={'placeholder':'Share for Groups'}))
	users = UserChoices(required=False, widget=AutoHeavySelect2MultipleWidget(
		select2_options = { 'minimumInputLength': 1, 'placeholder':'Share for Users' }))
	class Meta:
		model = Note
		widgets = { 'short_text': RedactorEditor(redactor_options={'buttons': "['html']",'linebreaks': True,'toolbar': True},allow_file_upload=False,allow_image_upload=False,),}
		fields = ['title', 'users', 'groups','short_text']
