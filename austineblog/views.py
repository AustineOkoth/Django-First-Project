from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

#Post.objects.get(pk=pk)


def post_list(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'austineblog/post_list.html', {'posts' : posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'austineblog/post_detail.html', {'post': post})