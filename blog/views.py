from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

def Post_list(request):
    data= Post.objects.all()
    return render (request,'post_list.html',{'posts':data})

class Postlist(ListView): #default : template --> post_list
    model=Post                     # object_list
    
#=======================
def post_Detail(request,post_id):
    data=Post.objects.get(id=post_id)
    return render(request,'post_info.html',{"post":data})

class PostDetail(DetailView):
    model=Post

#=======================
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

class PostCreate(CreateView):
    model=Post
    fields=['tilte','content','created_date','author','tags','draft','image']
    success_url='/blog'

#=======================
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

class PostUpdate(UpdateView):
    model=Post
    fields=['tilte','content','created_date','author','tags','draft','image']
    success_url='/blog'
    template_name='blog/post_update.html'
    
#========================
def delete_post(request,post_id):
    data=Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog')

class PostDelete(DeleteView):
    model=Post
    success_url='/blog'