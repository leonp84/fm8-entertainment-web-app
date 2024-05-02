from django.shortcuts import render, HttpResponse # noqa


# Create your views here.
def main(request):

    context = {
        'test': 'LeonTest'
    }

    return render(
        request,
        'main/index.html',
        context
    )


def movies(request):
    return render(
        request,
        'main/movies.html',
    )


def tv_series(request):
    return render(
        request,
        'main/tv-series.html'
    )


def bookmarked(request):
    return render(
        request,
        'main/bookmarked.html'
    )
