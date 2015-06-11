from django import forms
from redactor.widgets import RedactorEditor
from redactor.fields import RedactorField
from note.models import Note, NoteGroup
from groups.models import Group
from django_select2 import *
from django.contrib.auth.models import User
from IPython import embed

class UserChoices(AutoModelSelect2MultipleField):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		res = [(u.id, u.email) for u in User.objects.filter(email__icontains=term).exclude(id=request.user.id)]
		return NO_ERR_RESP, False, res

class GroupsChoices(AutoModelSelect2Field):
	queryset = User.objects
	search_fields = ['name__icontains', ]
	def get_results(self, request, term, page, context):
		res = [(v.id, v.email) for v in User.objects.filter(name__icontains=term).exclude(id=request.user.id)]
		return NO_ERR_RESP, False, res

class EditNoteForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Title"}))
	groups = ModelSelect2MultipleField(queryset=Group.objects, required=False, 
		widget=Select2MultipleWidget(attrs={'placeholder':'Share for Groups'}))
	users = UserChoices(required=False, widget=AutoHeavySelect2MultipleWidget(attrs={'placeholder':'Share for Users'}))
	class Meta:
		model = Note
		widgets = { 'short_text': RedactorEditor(),}
		fields = ['title', 'users', 'groups','short_text']
