from django.shortcuts import render
from .models import Movie, Role, Actor, Salary


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    for movie in movies:
        movie.roles = Role.objects.filter(movie_id=movie.id)
        for role in movie.roles:
            actors = Actor.objects.filter(role_id=role.id)
            role.actors = actors
            try:
                role.salary = Salary.objects.get(role_id=role.id)
            except Exception as e:
                role.salary = None

    context = {
        'movie_list': movies,
    }
    return render(request, 'movie/index.html', context)