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
		context['friendships'] = user.account.friends()
		context['invitations'] = user.account.invitations()
		return context

class AddFriendView(FormView):
	form_class = AddFriendForm
	template_name = "friends/add_friend_form.html"
	model = Friendship
	def form_valid(self, form):
		try:
			Friendship(creator=self.request.user.account, from_friend=self.request.user.account, 
						to_friend=form.cleaned_data['friend'].account).save()
			Friendship(creator=self.request.user.account, to_friend=self.request.user.account, 
						from_friend=form.cleaned_data['friend'].account).save()
		except IntegrityError:
			pass
		return HttpResponseRedirect(reverse('friends:index'))

class AcceptView(RedirectView):
	permanent = False
	query_string = True

	def get_redirect_url(self, pk, *args, **kwargs):
		friendship_invitation = get_object_or_404(Friendship, pk=pk)
		friendship_source = Friendship.objects.get(creator_id=friendship_invitation.creator.user_id, 
													to_friend_id=friendship_invitation.creator.user_id)
		friendship_invitation.confirmed = True
		friendship_invitation.save()
		friendship_source.confirmed = True
		friendship_source.save()
		return reverse('friends:index')

class DeleteView(DeleteView):
	model = Friendship
	def delete(self, request, *args, **kwargs):
		friends_ids = [ kwargs['pk'], self.request.user.id]
		deleting_objects = Friendship.objects.filter(from_friend__in=friends_ids, to_friend__in=friends_ids)
		if deleting_objects:
			deleting_objects.delete()
		return HttpResponseRedirect(reverse('friends:index'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

		
		