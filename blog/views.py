from django.shortcuts import render
from .models import Post

# Create your views here.

def Post_list(request):
    data= Post.objects.all()
    return render (request,'post_list.html',{'posts':data})

def post_info(request,post_id):
    data=Post.objects.get(id=post_id)
    return render(request,'post_info.html',{"post":data})