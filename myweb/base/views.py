from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Certif, User, Genre, Who, Comment
from django.db.models import Q
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, BookForms, UserForm
from .seeder import seeder_func
from django.contrib import messages




# Create your views here.


def home(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'base/about.html')


def article1(request):
    return render(request, 'base/article1.html')


def article2(request):
    return render(request, 'base/article2.html')


def article3(request, id):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    seeder_func()
    certifs = Certif.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(genre__name__icontains=q))
    certifs = list(dict.fromkeys(certifs))
    genres = Genre.objects.all()
    # certifs = certif.objects.all()
    context = {"certifs": certifs}
    heading = "წიგნები"
    context = {"certifs": certifs, "heading": heading, "genres": genres}
    print(certifs)
    return render(request, 'base/article3.html', context)


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    certifs = user.certifs.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(genre__name__icontains=q))
    certifs = list(set(certifs))
    genres = Genre.objects.all()

    heading = "My Certificats"
    context = {"certifs": certifs, "user": user,"heading": heading, "genres": genres}
    return render(request, 'base/profile.html', context)



def adding(request, id):
    certif = Certif.objects.get(id=id)
    user = request.user
    user.certifs.add(certif)
    return redirect('article3', user.id)



def delete(request, id):
    certif = Certif.objects.get(id=id)
    if request.method == "POST":
        request.user.certifs.remove(certif)
        return redirect('article3')
    return render(request, 'base/delete.html', {'obj': certif})



def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist!")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, "Username or Password is not correct!")

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')



def register_page(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')


    context = {'form': form}
    return render(request, 'base/register.html', context)


def add_book(request):
    whos = Who.objects.all()
    genres = Genre.objects.all()
    form = BookForms()

    if request.method == "POST":
        certif_who = request.POST.get('who')
        certif_genre = request.POST.get('genre')

        who, created = Who.objects.get_or_create(name=certif_who)
        genre, created = Genre.objects.get_or_create(name=certif_who)

        form = BookForms(request.POST)

        new_certif = Certif(picture=request.FILES['picture'], name=form.data['name'], who=who,
                            description=form.data['description'], file=request.FILES['file'], creator=request.user)

        if not (Certif.objects.filter(file=new_certif.file) or Certif.objects.filter(name=new_certif.name)):
            new_certif.save()
            new_certif.genre.add(genre)
            return redirect('home')



        return redirect('home')

    context = {'form': form, 'whos': whos, 'genres': genres}
    return render(request, 'base/add_book.html', context)

@login_required(login_url='login')
def reading(request, id):
    certif = Certif.objects.get(id=id)
    certif_comment = certif.comment_set.all().order_by('-created')
    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            certif=certif,
            body=request.POST.get('body')
        )
    return render(request, 'base/reading.html', {'certif': certif, 'comments':certif_comment})

def delete_certif(request, id):
    certif = Certif.objects.get(id=id)
    if request.method == 'POST':
        certif.picture.delete()
        certif.file.delete()
        certif.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': certif})

@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    return render(request, 'base/update_user.html', {'form': form})

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)

    certif = comment.certif
    if request.method == 'POST':
        comment.delete()
        return redirect('reading', certif.id)
    return render(request, 'base/delete.html', {'obj': comment})

