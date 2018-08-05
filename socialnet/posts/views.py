from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from . import forms
from django.utils.text import slugify

#TODO learn more about decorators in python
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post':post})

@login_required(login_url="/user/login/")
def post_new(request):
    #TODO once pages exist, redirect to the page that the post is being made to
    if request.method == 'POST':
        form = forms.NewPost(request.POST) #if file upload, add feild "request.FILES"
        if form.is_valid:
            instance = form.save(commit=False) #not saving until after a few changes
            instance.author = request.user
            instance.slug = slugify(str(request.user.id) + '17-' + instance.title)
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.NewPost()

    return render(request, 'posts/post_new.html', {'form':form})
