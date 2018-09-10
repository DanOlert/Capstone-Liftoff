from django.shortcuts import render, redirect
from posts.models import Post
from pages.models import Page
from user.models import UserSettings
from . import forms
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    if request.method == 'POST':
        form = forms.NewPost(request.POST) #if file upload, add feild "request.FILES"
        if form.is_valid:
            instance = form.save(commit=False) #not saving until after a few changes
            instance.author = request.user
            instance.authorslug = slugify(request.user.username + "-" + str(request.user.id))
            instance.slug = slugify(instance.title + '-' + str(instance.id))
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.NewPost()

    #TODO make the amount of entries per page changeable in settings
    posts = Post.objects.all().order_by('-date')[:23]
    return render(request, 'posts/post_list.html', {'posts': posts, 'form':form})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post':post})

@login_required(login_url="/user/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.NewPost(request.POST) #if file upload, add feild "request.FILES"
        if form.is_valid:
            instance = form.save(commit=False) #not saving until after a few changes
            instance.author = request.user
            instance.authorslug = slugify(request.user.username + "-" + str(request.user.id))
            instance.slug = slugify(instance.title + '-' + str(instance.id))
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.NewPost()

    return render(request, 'posts/post_new.html', {'form':form})
