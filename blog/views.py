from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def Post_list(request):
    data= Post.objects.all()
    return render (request,'post_list.html',{'posts':data})

def post_info(request,post_id):
    data=Post.objects.get(id=post_id)
    return render(request,'post_info.html',{"post":data})

def new_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform=request.user
            myform.save()
            return redirect('/blog')
    else:
        form=PostForm()
    return render(request,'new_post.html',{'form':form})

def edit_post(request,post_id):
    data=Post.objects.get(id=post_id)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform=form.save(commit=False)
            myform=request.user
            myform.save()
            return redirect('/blog')
    else:
        form=PostForm(instance=data)
    
    return render(request,'new_post.html',{'form':form})


def delete_post(request,post_id):
    data=Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog')