from django.shortcuts import render
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from django.views.generic.list import ListView
from friends.models import Friendship
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

class IndexView(ListView):
	model = Friendship
	template_name = "friends/index.html"
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		user = self.request.user
		context['creator_friends'] = Friendship.objects.filter(Q(friend=user), confirmed=True)
		context['invitated_friends'] = Friendship.objects.filter(Q(creator=user), confirmed=True)
		context['invitations'] = Friendship.objects.filter(Q(friend=user), confirmed=False)
		return context

class AddFriendView(FormView):
	form_class = AddFriendForm
	template_name = "friends/add_friend_form.html"
	model = Friendship
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(AddFriendView, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		email = form.cleaned_data['email']
		if email != self.request.user.email:
			try:
				user = User.objects.get(email=email)
				friendship = Friendship(creator=self.request.user, friend=user, confirmed=False)
				friendship.save()
				return HttpResponseRedirect(reverse('friends:index'))
			except:
				return HttpResponseRedirect(reverse('friends:add_friend'))
		else:
			return HttpResponseRedirect(reverse('friends:add_friend'))

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
		delete_object = Friendship.objects.get(pk=kwargs['pk'])
		if delete_object is not None:
			delete_object.delete()
		return HttpResponseRedirect(reverse('friends:index'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

		
		