from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.views.decorators.csrf import csrf_exempt

from DatabaseParking.forms import PostForm, DateForm
from DatabaseParking.models import Post, DatePost

@csrf_exempt
def post_list(request):
    posts=Post.objects.all()
    return render(request, 'park/post_list.html', {'posts':posts})

@csrf_exempt
def post_new(request):
    #print (request.data)
    #print (request.json)
    if request.method == "POST":
        print (request.body)
        print (request.body)
        fake = request.body
        fakedata = str(fake)
        print(fakedata)
        data=fakedata.split("'")[1]
        vn=data.split('=')[1].split('&')[0]
        vd=data.split('=')[2].split('&')[0]
        vt=data.split('=')[3].split('&')[0]
        va=data.split('=')[4]
        print (vn)
        print (vd)
        print(vt)
        print(va)
        sample=Post.objects.create(number=vn,date=vd,type=vt,amount=va,total=0)
        print (sample)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #print(post.type+ " "+ post.date+" "+post.amount+" "+post.number)
            p=get_object_or_404(Post,pk=post.pk)
            p.total=post.amount
            post.save()
            return redirect('post_list', number=post.number)
    else:
        form = PostForm()
    return render(request, 'park/post_new.html', {'form': form})

@csrf_exempt
def post_dates(request,pk):
    startDate=get_object_or_404(Post,pk=pk)
    dates=DatePost.objects.filter(number=pk)
    amount=get_object_or_404(Post,pk=pk).total
    return render(request,'park/post_dates.html',{'startDates':startDate,'dates':dates,'amount':amount})

@csrf_exempt
def post_add(request):
    if request.method == "POST":
        print (request.body)
        formatdata=str(request.body)
        data=formatdata.split("'")[1]
        vn=data.split('=')[1].split('&')[0]
        vd=data.split('=')[2].split('&')[0]
        va=data.split('=')[3]
        print(vn)
        print (vd)
        print (va)
        testkey=get_object_or_404(Post,pk=vn)
        sample=DatePost.objects.create(number=testkey,date=vd,amount=va)
        print (sample)
        form = DateForm(request.POST)
        print(request.body)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            #return redirect('post_list', number=post.number)
    else:
        form = DateForm()
    return render(request, 'park/post_add.html', {'form': form})