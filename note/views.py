from django.shortcuts import render
from note.forms import EditNoteForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from note.models import Note, NoteUser, NoteGroup
from groups.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.db.models import Q
from IPython import embed
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

class EditNoteView(UpdateView):
	form_class = EditNoteForm
	template_name = "note/add_note_form.html"
	model = Note
	def get_object(self):
		try: 
			return get_object_or_404(Note, pk=self.kwargs['pk'])
		except:
			return
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(EditNoteView, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return reverse('note:index')
	def form_valid(self, form):
		try:
			note = Note.objects.get(pk=self.kwargs['pk'])
			data = form.cleaned_data
			note.title = data['title']
			note.short_text = data['short_text']
			note.save()
			note.save_users_and_groups(data['users'], data['groups'])
		except KeyError:
			data = form.cleaned_data
			note = Note(owner=self.request.user, title=data['title'], short_text=data['short_text'])
			note.save()
			note.save_users_and_groups(data['users'], data['groups'])
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

class SharedNotesView(ListView):
	template_name = "note/shared_notes.html"
	model = NoteUser
	context_object_name = 'notes'
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(SharedNotesView, self).dispatch(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(SharedNotesView, self).get_context_data(**kwargs)
	 	user = self.request.user
	 	context['shared_notes'] = NoteUser.objects.filter(user_id=user.id)
	 	return context
		
		
