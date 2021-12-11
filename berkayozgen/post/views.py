from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.contrib import messages
from .models import Post
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(post_content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)     
        ).distinct()

    paginator = Paginator(post_list, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post/index.html', {'posts':page_obj})

def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = posts
        comment.save()
        return HttpResponseRedirect(posts.get_absolute_url())

    context = {

        'posts':posts,
        'form':form,
    }
    return render(request,'post/detail.html', context)

def post_create(request):

    if not request.user.is_authenticated:
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarılı Bir Şekilde Oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form':form,
    }    
    
    return render(request,'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    posts = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=posts)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı Bir Şekilde Düzenlediniz.')
        return HttpResponseRedirect(posts.get_absolute_url())
    context = {
        'form':form,
    } 
    return render(request,'post/form.html', context)

def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    posts = get_object_or_404(Post, slug=slug)
    posts.delete()
    return redirect('post:index')


