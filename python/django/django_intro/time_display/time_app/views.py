from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.


def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request, "index.html", context)
