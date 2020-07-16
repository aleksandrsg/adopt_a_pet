from django.shortcuts import render
from .models import Comment
from django.contrib.auth.decorators import login_required



# Create your views here.

def comments(request):
    comments = Comment.objects.all()
    context={
        'comments':comments
    }
    return render(request, 'blog/blog.html', context)

@login_required(login_url="/accounts/signin")
def new_comment(request):

    return render(request, 'blog/new_comment.html')