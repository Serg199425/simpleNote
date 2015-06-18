import json
from django.http import HttpResponse
from django.utils import timezone
from groups.models import GroupUser

def get_notifications(request):
    data = {}
    data['friends_invitations_count'] = request.user.account.invitations().count()
    data['unreaded_notes_count'] = request.user.account.shared_notes().filter(date__gte=request.user.account.shared_notes_last_seen).count()
    data['groups_invitations_count'] = GroupUser.objects.filter(user_id=request.user.id, confirmed=False).count()
    return HttpResponse(json.dumps(data), content_type = "application/json")