from django.shortcuts import render, redirect
from .models import Post
from .models import Category, Comments
from .forms import BlogComment, AddPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page_view(request):
    all_article=Post.objects.all()
    context={
        'articles':all_article
    }
    return render(request, "main/index.html", context)


# def contact_page_view(request):

    # return render(request, "main/contact.html")


def post_page_view(request, blog_id):
    blog_comment=BlogComment()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get("email")
        message=request.POST.get('message')
        Comments.objects.create(name=name, email=email, message=message)
    post=Post.objects.get(id=blog_id)
    category=Category.objects.all()
    comment=Comments.objects.all()
    related_post=Post.objects.filter(category=post.category).exclude(id=post.id)
    context={
        'post':post,
        'category':category,
        'related':related_post,
        'comment':comment,
        'blog_comment':blog_comment
    }

    return render(request, "main/post.html", context)

@login_required
def add_post(request):
    forms= AddPostForm()
    if request.method == 'POST':
        forms=AddPostForm(request.POST, request.FILES)
        if forms.is_valid():
            # forms.save(owner= request.user)
            post=forms.save(commit = False)
            post.owner=request.user
            post.save()
            messages.success(request,"Your Post has been added successfully!")
            return redirect('home')
    context={
        "forms":forms
    }
   
    return render(request, "main/add_post.html", context)
