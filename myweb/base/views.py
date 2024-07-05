from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Certif, User, Genre
from django.db.models import Q
from django.contrib.auth import authenticate,login, logout


# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def about(request):
    return render(request, 'base/about.html')


def article1(request):
    return render(request, 'base/article1.html')


def article2(request):
    return render(request, 'base/article2.html')


def article3(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    certifs = Certif.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(genre__name__icontains=q))
    certifs = list(set(certifs))
    genres = Genre.objects.all()
    # certifs = certif.objects.all()
    context = {"certifs": certifs}
    heading = "Certificats"
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
    return redirect('article3')



def delete(request, id):
    certif = Certif.objects.get(id=id)
    if request.method == "POST":
        request.user.certifs.remove(certif)
        return redirect('article3')
    return render(request, 'base/delete.html', {'certif': certif})



def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            pass #  Error Message...

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             pass #ერორის მესიჯი
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')



def register_page(request):
    context = {}
    return render(request, 'base/login_register.html', context)