from django.shortcuts import render
from note.forms import AddNoteForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from note.models import Note

class AddNoteView(FormView):
	form_class = AddNoteForm
	template_name = "note/add_note_form.html"
	def get_initial(self):
		user = self.request.user
	def form_valid(self, form):
		short_text = form.cleaned_data['short_text']
		title = form.cleaned_data['short_text']
		user = self.request.user
		note = Note(owner=user, title=title, short_text=short_text)
		note.save()
		return HttpResponseRedirect(reverse('note:index'))

class IndexView(ListView):
	template_name = "note/index.html"
	model = Note
	context_object_name = 'notes'

def delete(request, note_id):
	try:
		note = Note.objects.get(id=note_id)
		note.delete()
		return HttpResponseRedirect(reverse('note:index'))
	except User.DoesNotExist:
		return HttpResponseRedirect(reverse('note:index'))
	
