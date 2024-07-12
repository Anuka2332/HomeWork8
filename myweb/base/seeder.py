from .models import Who, Genre

def seeder_func():
    whos = ['მარიამ ებანნოიძე', 'ელენე აბაშიძე', 'ლანა ზირაქაძე']
    genres = ['ტრენინგი', 'ონლაინ კურსი', 'პროფესიული სერთიფიკატი']

    for who in whos:
        if not Who.objects.filter(name=who):
            new_who = Who(name=who)
            new_who.save()

    for genre in genres:
        if not Genre.objects.filter(name=genre):
            new_genre = Genre(name=genre)
            new_genre.save()
