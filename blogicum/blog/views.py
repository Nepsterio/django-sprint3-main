from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .constants import POSTS_MAX
from .models import Category, Post


def get_base_queryset():
    current_time = now()
    return Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).select_related('category', 'author', 'location').order_by('-pub_date')


def index(request):
    posts = posts = get_base_queryset()[:POSTS_MAX]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(get_base_queryset(), id=id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug,
        is_published=True
    )
    posts = get_base_queryset().filter(category=category)
    context = {'post_list': posts, 'category': category}

    return render(request, 'blog/category.html', context)
