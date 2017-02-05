from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'website/post.html', {'post': post})

def index(request):
    posts_list = Post.objects.order_by('-created_at')
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'website/index.html', {'posts': posts})



