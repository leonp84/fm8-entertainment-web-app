from django.shortcuts import render, HttpResponse # noqa
from .models import Movie
from django.http import JsonResponse


# Create your views here.
def main(request):
    trending = Movie.objects.all().filter(isTrending=True)
    recommended = Movie.objects.all().filter(isTrending=False)
    context = {
        'trending': trending,
        'recommended': recommended,
    }
    return render(
        request,
        'main/index.html',
        context
    )


def movies(request):
    movie_items = Movie.objects.all().filter(category='Movie')
    return render(
        request,
        'main/movies.html',
        {'movie_items': movie_items}
    )


def tv_series(request):
    tv_items = Movie.objects.all().filter(category='TV Series')
    return render(
        request,
        'main/tv-series.html',
        {'tv_items': tv_items}
    )


def bookmarked(request):
    bookmarked_items = Movie.objects.all().filter(isBookmarked=True)
    return render(
        request,
        'main/bookmarked.html',
        {'bookmarked_items': bookmarked_items}
    )


def update_bookmarks(request):

    for item, value in request.headers.items():
        if item == 'Item':
            update_item = value

    to_update = Movie.objects.all().filter(title=update_item).first()
    if to_update.isBookmarked:
        to_update.isBookmarked = False
    else:
        to_update.isBookmarked = True
    to_update.save()

    return JsonResponse({'message': 'Model Updated'})
