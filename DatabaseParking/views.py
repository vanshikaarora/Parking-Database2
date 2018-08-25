from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.views.decorators.csrf import csrf_exempt

from DatabaseParking.forms import PostForm, DateForm
from DatabaseParking.models import Post, DatePost


def post_list(request):
    posts=Post.objects.all()
    return render(request, 'park/post_list.html', {'posts':posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_list', number=post.number)
    else:
        form = PostForm()
    return render(request, 'park/post_new.html', {'form': form})


def post_dates(request,pk):
    startDate=get_object_or_404(Post,pk=pk)
    dates=DatePost.objects.filter(number=pk)
    return render(request,'park/post_dates.html',{'startDates':startDate,'dates':dates})


def post_add(request):
    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_list', number=post.number)
    else:
        form = DateForm()
    return render(request, 'park/post_add.html', {'form': form})