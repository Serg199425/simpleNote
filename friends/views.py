from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from account.models import Friendship
from django.db.models import Q
from friends.forms import *
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from IPython import embed
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django.db import IntegrityError

class IndexView(ListView):
	model = Friendship
	template_name = "friends/index.html"
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		user = self.request.user
		context['friends'] = user.account.friends()
		context['invitations'] = user.account.invitations()
		return context

class AddFriendView(FormView):
	form_class = AddFriendForm
	template_name = "friends/add_friend_form.html"
	model = Friendship
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(AddFriendView, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		try:
			Friendship(creator=self.request.user, friend=form.cleaned_data['friend'], confirmed=False).save()
		except IntegrityError:
			pass
		return HttpResponseRedirect(reverse('friends:index'))

class AcceptView(RedirectView):
	permanent = False
	query_string = True

	def get_redirect_url(self, pk, *args, **kwargs):
		friendship = get_object_or_404(Friendship, pk=pk)
		friendship.confirmed = True
		friendship.save()
		return reverse('friends:index')

class DeleteView(DeleteView):
	model = Friendship
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(DeleteView, self).dispatch(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		delete_object = Friendship().get(user_id=kwargs['pk'], current_user_id=self.request.user.id)
		if delete_object is not None:
			delete_object.delete()
		return HttpResponseRedirect(reverse('friends:index'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

		
		