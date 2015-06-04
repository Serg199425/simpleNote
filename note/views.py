from django.shortcuts import render
from note.forms import EditNoteForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from note.models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/login/')

class EditNoteView(LoginRequiredMixin, FormView):
	form_class = EditNoteForm
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

class IndexView(LoginRequiredMixin, ListView):
	template_name = "note/index.html"
	model = Note
	context_object_name = 'notes'

@login_required(login_url='/login/')
def delete(request, note_id):
	try:
		note = Note.objects.get(id=note_id)
		note.delete()
		return HttpResponseRedirect(reverse('note:index'))
	except User.DoesNotExist:
		return HttpResponseRedirect(reverse('note:index'))
	
