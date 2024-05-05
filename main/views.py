from django.shortcuts import render, HttpResponse # noqa
from .models import Movie
from django.http import JsonResponse


# Create your views here.
def main(request):
    trending = Movie.objects.all().filter(isTrending=True)
    recommended = Movie.objects.all().filter(isTrending=False)

    if request.method == 'POST':
        user_input = request.POST['user-input']
        search_results = Movie.objects.all().filter(
            title__icontains=user_input)
        return render(
            request,
            'main/index.html',
            {'recommended': search_results,
             'user_input': user_input}
        )

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

    if request.method == 'POST':
        search_results = Movie.objects.all().filter(
            title__icontains=request.POST['user-input'], category='Movie')
        print(search_results)
        return render(
            request,
            'main/movies.html',
            {'movie_items': search_results}
        )

    return render(
        request,
        'main/movies.html',
        {'movie_items': movie_items}
    )


def tv_series(request):
    tv_items = Movie.objects.all().filter(category='TV Series')

    if request.method == 'POST':
        search_results = Movie.objects.all().filter(
            title__icontains=request.POST['user-input'], category='TV Series')
        print(search_results)
        return render(
            request,
            'main/movies.html',
            {'movie_items': search_results}
        )

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

    if request.method == 'POST':
        bookmarked_items_movies = Movie.objects.all().filter(
            title__icontains=request.POST[
                'user-input'], isBookmarked=True, category='Movie')
        bookmarked_items_tv = Movie.objects.all().filter(
            title__icontains=request.POST[
                'user-input'], isBookmarked=True, category='TV Series')
        return render(
            request,
            'main/bookmarked.html',
            {'bookmarked_items_movies': bookmarked_items_movies,
             'bookmarked_items_tv': bookmarked_items_tv}
        )

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
