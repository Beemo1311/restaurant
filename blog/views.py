
from urllib import request
from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import CommentForm
from taggit.models import Tag
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'post_list': post_list,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post_detail)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        'post_detail': post_detail,
        'categories': categories,
        'comments': comments,
        'all_tags': all_tags,
        'comment_form': comment_form
    }
    return render(request, '', context)

def post_by_category(request, category):
    post_by_category = Post.objects.filter(category__category_name = category)
    context = {
        'post_list': post_by_category
    }
    return render(request, 'post_list.html', context)

def post_by_tag(request, tag):
    post_by_tag = Post.objects.filter(tags__name_in = [tag])
    context = {
        'post_list' : post_by_tag
    }
    return render(request, 'post_list.html', context)