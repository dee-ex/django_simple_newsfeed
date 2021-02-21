import re
import json

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.feed.models import Post, Like
from apps.conversation.models import ConversationMessage
from apps.notification.services import create_notification

@login_required
def add_post(request):
    data = json.loads(request.body)
    body = data['body']

    post = Post.objects.create(body=body, created_by=request.user)

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)

    for result in results:
        word = result[1]

        if User.objects.filter(username=word).exists() and word != request.user.username:
            create_notification(request, User.objects.get(username=word), 'mention')

    return JsonResponse({'success': True})

@login_required
def add_like(request):
    data = json.loads(request.body)
    post_id = data['post_id']

    if not Like.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
        like = Like.objects.create(post_id=post_id, created_by=request.user)
        post = Post.objects.get(pk=post_id)
        create_notification(request, post.created_by, 'like')

    return JsonResponse({'success': True})

@login_required
def add_message(request):
    data = json.loads(request.body)
    content = data['content']
    conversation_id = data['conversation_id']


    message = ConversationMessage.objects.create(conversation_id=conversation_id, content=content, created_by=request.user)

    to_user = None

    for user in message.conversation.users.all():
        if user != request.user:
            create_notification(request, user, 'message')

    return JsonResponse({'success': True})