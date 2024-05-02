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
