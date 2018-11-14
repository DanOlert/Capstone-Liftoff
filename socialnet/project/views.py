from django.shortcuts import render, redirect

# Create your views here.
def project_demo(request):

    return render(request, 'project/project_demo.html')

def project_new(request):

    return render(request, 'project/project_demo.html')

def project_detail(request, slug):
    # TODO: how to render individual slugs (replace "post" with "project")
    # post = Post.objects.get(slug=slug)
    # return render(request, 'posts/post_detail.html', {'post':post})
    return render(request, 'project/project_demo.html')
