from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from apps.notification.services import create_notification

from .forms import SnewsfeedProfileForm

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()

    for post in posts:
        likes = post.likes.filter(created_by_id=request.user.id)

        # post.liked = likes.count() == 1
        post.liked = likes.count() > 0

    context = {
        'user': user,
        'posts': posts
    }

    return render(request, 'profile/profile.html', context=context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = SnewsfeedProfileForm(request.POST, request.FILES, instance=request.user.snewsfeedprofile)

        if form.is_valid():
            form.save()

            return redirect('profile', username=request.user.username)

    form = SnewsfeedProfileForm(instance=request.user.snewsfeedprofile)

    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'profile/edit_profile.html', context)


@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)

    request.user.snewsfeedprofile.follows.add(user.snewsfeedprofile)

    create_notification(request, user, 'follower')

    return redirect('profile', username=username)

@login_required
def unfollow(request, username):
    user = get_object_or_404(User, username=username)

    request.user.snewsfeedprofile.follows.remove(user.snewsfeedprofile)

    return redirect('profile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/followers.html', {'user': user})


def follows(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/follows.html', {'user': user})