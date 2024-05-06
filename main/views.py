from django.shortcuts import render, HttpResponse  # noqa
from django.http import JsonResponse
from .models import Movie


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
    bookmarked_items_movies = Movie.objects.all().filter(
        isBookmarked=True, category='Movie')
    bookmarked_items_tv = Movie.objects.all().filter(
        isBookmarked=True, category='TV Series')

    return render(
        request,
        'main/bookmarked.html',
        {'bookmarked_items_movies': bookmarked_items_movies,
         'bookmarked_items_tv': bookmarked_items_tv,
         }
    )


def update_bookmarks(request):

    for item, value in request.headers.items():
        if item == 'Item':
            update_item = value

    to_update = Movie.objects.all().filter(id=update_item).first()
    if to_update.isBookmarked:
        to_update.isBookmarked = False
    else:
        to_update.isBookmarked = True
    to_update.save()
    print(to_update.title + 'Bookmarked = ' + str(to_update.isBookmarked))

    return JsonResponse({'message': 'Model Updated'})


def search(request):
    if request.method == 'POST':
        user_input = request.POST['user-input']
        search_results = Movie.objects.all().filter(
            title__icontains=user_input)
        return render(
            request,
            'main/search.html',
            {'search_items': search_results,
             'user_input': user_input}
        )


def login(request):

    if request.method == 'POST':
        return render(
            request,
            'main/index.html')

    return render(
        request,
        'main/login.html')


def sign_up(request):
    return render(
        request,
        'main/sign-up.html')
