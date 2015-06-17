from django.shortcuts import render
from note.forms import EditNoteForm
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from note.models import Note, NoteUser, NoteGroup, FavoriteNote
from groups.models import Group
from django.views.generic.detail import DetailView
from django.db.models import Q
from IPython import embed
from account.models import User
from django.shortcuts import get_object_or_404

class EditNoteView(UpdateView):
	form_class = EditNoteForm
	template_name = "note/add_note_form.html"
	model = Note
	def get_object(self):
		try: 
			return get_object_or_404(Note, pk=self.kwargs['pk'])
		except:
			return
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
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
	 	user = self.request.user
	 	context['notes'] = Note.objects.filter(owner_id=user.id)
	 	context['favorite_notes'] = user.favorite_notes.all()
	 	return context

class DeleteView(DeleteView):
	model = Note
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

class SharedNotesView(ListView):
	template_name = "note/shared_notes.html"
	model = NoteUser
	context_object_name = 'notes'
	def get_context_data(self, **kwargs):
		context = super(SharedNotesView, self).get_context_data(**kwargs)
	 	user = self.request.user
	 	context['shared_notes'] = user.account.shared_notes()
	 	context['favorite_notes'] = self.request.user.favorite_notes.all()
	 	return context

class AddFavoriteView(RedirectView):
	permanent = False
	query_string = False
	def get_redirect_url(self, pk):
		note = get_object_or_404(Note, pk=pk)
		FavoriteNote(note_id=note.id, user_id=self.request.user.id).save()
		return self.request.META.get('HTTP_REFERER','/')

class RemoveFavoriteView(DeleteView):
	model = FavoriteNote
	def delete(self, request, *args, **kwargs):
		delete_object = FavoriteNote.objects.get(note_id=kwargs['pk'], user_id=self.request.user.id)
		delete_object.delete()
		return HttpResponseRedirect(self.request.META.get('HTTP_REFERER','/'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

class FavoriteIndexView(ListView):
	template_name = "note/favorite_index.html"
	model = FavoriteNote
	context_object_name = 'favorite_notes'
	def get_context_data(self, **kwargs):
		context = super(FavoriteIndexView, self).get_context_data(**kwargs)
	 	context['notes'] = self.request.user.favorite_notes.all()
	 	return context
		
		
