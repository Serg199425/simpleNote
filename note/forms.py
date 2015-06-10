from django import forms
from redactor.widgets import RedactorEditor
from redactor.fields import RedactorField
from note.models import Note, NoteGroup
from groups.models import Group
from django_select2 import *
from django.contrib.auth.models import User

class EditNoteForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Title"}))
	groups = ModelSelect2MultipleField(queryset=Group.objects, required=False, 
		widget=Select2MultipleWidget(attrs={'placeholder':'Share for Groups'}))
	users = ModelSelect2MultipleField(queryset=User.objects, required=False, 
		widget=Select2MultipleWidget(attrs={'placeholder':'Share for Users'}))
	class Meta:
		model = Note
		widgets = { 'short_text': RedactorEditor(),}
		fields = ['title', 'users', 'groups','short_text']