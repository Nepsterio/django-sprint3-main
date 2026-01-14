from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.timezone import now
from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    current_time = now()
    posts = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]

    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    current_time = now()
    template = 'blog/detail.html'
    try:
        post = get_object_or_404(Post, id=id,
                                 pub_date__lte=current_time,
                                 is_published=True,
                                 category__is_published=True)
    except Post.DoesNotExist:
        raise Http404("Публикация не найдена.")
    context = {'post': post}

    return render(request, template, context)


def category_posts(request, category_slug):
    current_time = now()
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    template = 'blog/category.html'
    posts = Post.objects.filter(
        category=category,
        pub_date__lte=current_time,
        is_published=True
    ).order_by('-pub_date')
    context = {'post_list': posts, 'category': category}

    return render(request, template, context)
