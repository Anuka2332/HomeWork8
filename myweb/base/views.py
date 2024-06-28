from django.shortcuts import render
from django.http import HttpResponse
from .models import certif, User

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
    certifs = certif.objects.all()
    context = {"certifs": certifs}

    print(certifs)
    return render(request, 'base/article3.html', context)


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    certifs = user.certifs.all()
    context = {"certifs": certifs, "user": user}
    return render(request, 'base/profile.html', context)
