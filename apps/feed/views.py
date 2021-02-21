from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post

@login_required
def feed(request):
    userids = [request.user.id]

    for creater in request.user.snewsfeedprofile.follows.all():
        userids.append(creater.user.id)

    posts = Post.objects.filter(created_by_id__in=userids)

    for post in posts:
        likes = post.likes.filter(created_by_id=request.user.id)

        post.liked = likes.count() > 0

    return render(request, 'feed/feed.html', context={'posts': posts})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        users = User.objects.filter(username__icontains=query)
        posts = Post.objects.filter(body__icontains=query)
    else:
        users = []
        posts = []

    context = {
        'query': query,
        'users': users,
        'posts': posts
    }

    return render(request, 'feed/search.html', context=context)