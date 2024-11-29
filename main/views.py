from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import RegistrationForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Post, UserC, School


@login_required(login_url='/login')
def home(request):

    school = request.user.school_id
    posts = Post.objects.filter(school=school).order_by('-created')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.school_id = request.user.school_id
            post.save()

            return redirect('/')
    else:
        form = PostForm()    
    
    return render(request, 'main/home.html', {'posts': posts, 'form': form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='/')
def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'main/createpost.html', {'form': form})




@login_required(login_url='/')
def members(request):
    usernames = UserC.objects.all().values()

    return render(request, 'main/members.html', {'usernames': usernames})

@login_required(login_url='/')
def user(request, id):

    userpag = UserC.objects.get(id=id)

    posts = userpag.posts.all().order_by('-created')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.user_id = userpag.id
            post.save()

            return redirect('/')
    else:
        form = PostForm()  

    return render(request, 'main/user.html', {'userpag': userpag,
                                                'posts': posts,
                                                'form': form})




@login_required(login_url='/')
def schools(request):
    schools = School.objects.all().values()

    return render(request, 'main/schools.html', {'schools': schools})



@login_required(login_url='/')
def school(request, id):

    school = School.objects.get(id=id)
    posts = school.posts.all().order_by('-created')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.school_id = school.id
            post.save()

            return redirect('/')
    else:
        form = PostForm()  

    return render(request, 'main/school.html', {'school': school,
                                                'posts': posts,
                                                'form': form})




