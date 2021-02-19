from bbs.models import Post
from bbs.forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404


def p_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'bbs/list.html',
                  {'posts': posts})


def p_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('bbs:p_list')

    if request.method == 'GET':
        post_form = PostForm()
        return render(request, 'bbs/create.html', {'post_form': post_form})






