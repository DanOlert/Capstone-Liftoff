from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.utils.text import slugify
from django.db.models import Q

from .models import UserSettings

from pages.models import Page
from posts.models import Post

from posts import forms as formsPosts
from pages import forms as formsPages
from . import forms

#TODO learn more about decorators in python
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
    #TODO allow first and last names as well as emails, see signup.html
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #saves new user and adds sets user variable
            login(request, user)
#TODO Make settings actually save in database ugh
            settings = UserSettings() #saves a persistant settings file for user
            settings.user = request.user
            settings.title = (request.user.username + "'s Settings")
            settings.save()
            return redirect('user:edit')
    else:
        form = UserCreationForm()

    return render(request, 'user/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')
    else:
        form = AuthenticationForm()

    return render(request,'user/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/posts/')

@login_required(login_url="/user/login/")
def edit_my_page(request):
    current_user = request.user
    if request.method == 'POST':
        form = formsPages.EditPage(request.POST) #if file upload, add feild "request.FILES"
        if form.is_valid:
             instance = form.save(commit=False) #not saving until after a few changes
             instance.owner = current_user
             instance.type = ("User")
             instance.slug = slugify(current_user.username + "-" + str(current_user.id))
             #TODO save image
             instance.save()
             return redirect('user:view', slug=str(instance.slug))
    else:
        if Page.objects.filter(slug=slugify(current_user.username + "-" + str(current_user.id))).exists():
            page = Page.objects.get(slug=slugify(current_user.username + "-" + str(current_user.id)))
            form = formsPages.EditPage()
            return render(request, 'edit_page.html', {'form':form, 'current_user':current_user, 'page':page})
        else:
            form = formsPages.EditPage()

    return render(request, 'edit_page.html', {'form':form, 'current_user':current_user})

@login_required(login_url="/user/login/")
def my_page(request):
    slug = slugify(request.user.username + "-" + str(request.user.id))
    return redirect('user:view', slug=slug)

def page_view(request, slug):
    if Page.objects.filter(slug=slug).exists():
        page = Page.objects.get(slug=slug)
        if request.method == 'POST':
            form = formsPosts.NewPost(request.POST) #if file upload, add feild "request.FILES"
            if form.is_valid:
                instance = form.save(commit=False) #not saving until after a few changes
                instance.author = request.user
                instance.authorslug = slugify(request.user.username + "-" + str(request.user.id))
                instance.slug = slugify(instance.title + '-' + str(instance.id))
                instance.page = page
                instance.save()
        else:
            form = formsPosts.NewPost()
        posts = Post.objects.filter(Q(page=page) | Q(author=page.owner)).order_by('-date')[:11]
    else:
        if slug==slugify(request.user.username + "-" + str(request.user.id)):
            return render(request, 'you_have_no_page.html')

        return render(request, 'no_page.html')

    return render(request, 'view_page.html', {'page': page, 'posts': posts, 'form':form})

def page_view_projects(request, slug):
    if Page.objects.filter(slug=slug).exists():
        page = Page.objects.get(slug=slug)
    else:
        if slug==slugify(request.user.username + "-" + str(request.user.id)):
            return render(request, 'you_have_no_page.html')

        return render(request, 'no_page.html')

    return render(request, 'projects.html', {'page': page})


    # if Page.objects.filter(slug=(slugify(str(request.user.id) + '17'))).exists():
    #     page = Page.objects.get(slug=slug)
    #     return render(request, 'user/page_view.html', {'page':page})
    # else:
    #     return ("no page here")
