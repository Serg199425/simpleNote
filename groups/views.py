from django.shortcuts import render
from account.models import User
from django.views.generic.list import ListView
from account.models import Friendship
from django.db.models import Q
from groups.forms import AddGroupForm, AddUserToGroupForm
from django.views.generic.edit import FormView, UpdateView
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
from django.http import HttpResponse
from django.template.loader import render_to_string
import json
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
	def form_valid(self, form):
		group = Group(name=form.cleaned_data['name'], creator_id=self.request.user.id)
		group.save()
		GroupUser(group_id=group.id, user_id=self.request.user.id, confirmed=True, is_creator=True).save()
		for user in form.cleaned_data['users']:
			GroupUser(group_id=group.id, user_id=user.id, confirmed=False, is_creator=False).save()
		return HttpResponseRedirect(reverse('groups:index'))


class AddUserToGroupView(UpdateView):
	form_class = AddUserToGroupForm
	template_name = "groups/add_user_to_group_form.html"
	model = Group
	def get_object(self):
		group = Group.objects.get(pk=self.kwargs['pk'])
		form = AddUserToGroupForm(initial={'users': group.users.exclude(pk=group.creator_id)})
		try:
			return get_object_or_404(Group, pk=self.kwargs['pk'])
		except:
			return
	def form_valid(self, form):
		try:
			group = Group.objects.get(pk=self.kwargs['pk'])
			group.groupuser_set.all().delete()
			GroupUser(group_id=group.id, user_id=group.creator_id, confirmed=True, is_creator=True).save()
			for user in form.cleaned_data['users']:
				GroupUser(group_id=group.id, user_id=user.id, confirmed=False, is_creator=False).save()	
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
		context['group_users'] = GroupUser.objects.filter(group_id=self.kwargs['pk'])
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
	def delete(self, request, *args, **kwargs):
		delete_object = Group.objects.get(pk=kwargs['pk'])
		if delete_object is not None:
			delete_object.delete()
		return HttpResponseRedirect(reverse('groups:index'))
	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

class DeleteGroupUserView(DeleteView):
	model = GroupUser
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

def get_groups_invitations(request):
	invitations = GroupUser.objects.filter(user_id=request.user, confirmed=False)
	html = render_to_string("groups/invitations_list.html", { 'invitations': invitations, })
	data = {}
	data['html'] = html
	return HttpResponse(json.dumps(data), content_type = "application/json")


		
		