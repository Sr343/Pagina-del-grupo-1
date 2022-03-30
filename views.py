from django.http import HttpResponse
from django.shortcuts import render 

from blog.models import Post
def index(request):
    Posts = Post.objects.all()
   # return HttpResponse ('wenaaaas chavales')
    return render(request, 'index.html', {
        'Posts':Posts,
    })
    

def about (request):
   
    return render(request, 'about.html', {})