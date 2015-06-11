from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from account.models import Friendship
from django.db.models import Q
from groups.forms import AddGroupForm, AddUserToGroupForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from note.models import Note
from groups.models import Group, GroupUser
from IPython import embed

class IndexView(ListView):
	model = GroupUser
	template_name = "groups/index.html"
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		user = self.request.user
		context['group_users'] = GroupUser.objects.filter(user_id=user.id, confirmed=True)
		context['invitations'] = GroupUser.objects.filter(user_id=user.id, confirmed=False)
		return context

class AddView(FormView):
	form_class = AddGroupForm
	template_name = "groups/add_group_form.html"
	model = Group
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(AddView, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		group = Group(name=form.cleaned_data['name'], creator_id=self.request.user.id)
		group.save()
		GroupUser(group_id=group.id, user_id=self.request.user.id, confirmed=True, is_creator=True).save()
		return HttpResponseRedirect(reverse('groups:index'))


class AddUserToGroupView(FormView):
	form_class = AddUserToGroupForm
	template_name = "groups/add_user_to_group_form.html"
	model = GroupUser
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(AddUserToGroupView, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		try:
			group = Group.objects.get(pk=self.kwargs['pk'])
			GroupUser(group_id=group.id, user_id=form.cleaned_data['user'].id).save()
			return HttpResponseRedirect(reverse('groups:index'))
		except Group.DoesNotExist:
			return HttpResponseRedirect(reverse('groups:index'))
		except:
			return HttpResponseRedirect(reverse('groups:index'))

class ShowGroupUsersView(ListView):
	model = GroupUser
	template_name = "groups/group_users.html"
	def get_context_data(self, **kwargs):
		context = super(ShowGroupUsersView, self).get_context_data(**kwargs)
		context['group_users'] = GroupUser.objects.filter(group_id=self.kwargs['pk'],confirmed=True)
		context['current_group'] = Group.objects.get(pk=self.kwargs['pk'])
		return context

class AcceptView(RedirectView):
	permanent = False
	query_string = True

	def get_redirect_url(self, pk, *args, **kwargs):
		group_user = get_object_or_404(GroupUser, pk=pk)
		group_user.confirmed = True
		group_user.save()
		return reverse('groups:index')

class DeleteView(DeleteView):
	model = Group
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(DeleteView, self).dispatch(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		delete_object = Group.objects.get(pk=kwargs['pk'])
		if delete_object is not None:
			delete_object.delete()
		return HttpResponseRedirect(reverse('groups:index'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

class DeleteGroupUserView(DeleteView):
	model = GroupUser
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, request, *args, **kwargs):
		return super(DeleteGroupUserView, self).dispatch(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		try:
			delete_object = GroupUser.objects.get(pk=kwargs['pk'])
			if delete_object is not None:
				delete_object.delete()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
		except:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

		
		