from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto in ('conversation', 'profile'):
        notification = Notification.objects.get(pk=notification_id)
        notification.is_checked = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('conversation', userid=notification.created_by.id)

        if notification.notification_type == Notification.FOLLOWER:
            return redirect('profile', username=notification.created_by.username)

        if notification.notification_type == Notification.LIKE:
            return redirect('profile', username=notification.to_user.username)

        if notification.notification_type == Notification.MENTION:
            return redirect('profile', username=notification.created_by.username)

    return render(request, 'notification/notifications.html')