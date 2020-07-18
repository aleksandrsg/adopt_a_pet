from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.decorators import login_required
from . import forms 


# Create your views here.

def comments(request):
    comments = Comment.objects.all()
    context={
        'comments':comments
    }
    return render(request, 'blog/blog.html', context)

@login_required(login_url="/accounts/signin")
def new_comment(request):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            addition = form.save(commit=False)
            addition.author = request.user
            addition.save()
            return redirect('home')
    else:
        form = forms.CreateComment()
        context = {
            'form':form
        }
    return render(request, 'blog/new_comment.html', context)