from django.shortcuts import render
from note.forms import EditNoteForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from note.models import Note
from friends.models import Friendship
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.db.models import Q
from IPython import embed

class EditNoteView(FormView):
	form_class = EditNoteForm
	template_name = "note/add_note_form.html"
	model = Note
	def get_initial(self):
		user = self.request.user
		try:
			note = Note.objects.get(pk=self.kwargs['pk'])
			return {'title': note.title, 'short_text': note.short_text }
		except:
			return
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(EditNoteView, self).dispatch(request, *args, **kwargs)
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
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(IndexView, self).dispatch(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
	 	user = self.request.user
	 	context['notes'] = Note.objects.filter(owner_id=user.id)
	 	context['invitations_count'] = Friendship.objects.filter(Q(friend=user), confirmed=False).count
	 	return context

class DeleteView(DeleteView):
	model = Note
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(DeleteView, self).dispatch(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		delete_object = Note.objects.get(pk=kwargs['pk'])
		if delete_object is not None:
			delete_object.delete()
		return HttpResponseRedirect(reverse('note:index'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

class ShowView(DetailView):
	template_name = "note/show.html"
	model = Note
	context_object_name = 'note'
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(ShowView, self).dispatch(request, *args, **kwargs)
