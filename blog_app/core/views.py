from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect

from .form import *
from .models import *
from django.contrib.auth.models import Group


# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {
                'error': 'Error'
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def user_register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            email_field = str(request.POST['email'])
            if email_field.endswith('@admin.com'):
                user.is_superuser = True
                user.is_staff = True
                user.save()
            else:
                selected_group = Group.objects.get(name='user')
                user.groups.add(selected_group)
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


# ----------------- BLOG CRUD-----------------------
@login_required
@permission_required('core.blog.can_create_blog', raise_exception=PermissionError)
def blog_create(request):
    form = BlogForm

    user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = user
            form.save()
            return redirect('blogs')
    context = {
        'form': form,
    }
    return render(request, 'blog/blog_create.html', context)


@login_required
def blogs_read(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blogs.html', context)


@login_required
@permission_required('core.blog.can_change_blog', raise_exception=PermissionError)
def blog_update(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, 'blog/blog_update.html', context)


@login_required
@permission_required('core.blog.can_delete_blog', raise_exception=PermissionError)
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    return redirect('blogs')


@login_required
def blog_details(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_details.html', context)




@login_required
def log_out(request):
    logout(request)
    return redirect('login')

def query(request):
    blog= Blog.objects.all()
    print(blog)
    user=Blog.objects.get(id=5)
    coneext = {
        'user': user
    }
    print(user)
    return redirect('login')

