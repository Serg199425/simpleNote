from django import forms
from redactor.widgets import RedactorEditor
from redactor.fields import RedactorField
from note.models import Note, NoteGroup
from groups.models import Group
from account.models import User
from account.forms import UserChoices
from django_select2 import AutoModelSelect2MultipleField, AutoHeavySelect2MultipleWidget
from tagging.forms import TagField
from tagging_autocomplete_tagit.widgets import TagAutocompleteTagIt
from IPython import embed

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
	tags = TagField(widget=TagAutocompleteTagIt(max_tags=5), required=False)
	class Meta:
		model = Note
		widgets = { 'short_text': RedactorEditor(redactor_options={'buttons': "['html']",'linebreaks': True,'toolbar': True},allow_file_upload=False,allow_image_upload=False,),}
		fields = ['title', 'tags','users', 'groups','short_text']
