from django.shortcuts import render
from django.http import HttpResponse
from .models import certif, User, Genre
from django.db.models import Q


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

    certifs = certif.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(genre__name__icontains=q))
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
