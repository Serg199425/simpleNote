from django import forms
from redactor.widgets import RedactorEditor
from redactor.fields import RedactorField
from note.models import Note

class AddNoteForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Title"}))
	class Meta:
		model = Note
		widgets = { 'short_text': RedactorEditor(),}
		fields = ['title','short_text']