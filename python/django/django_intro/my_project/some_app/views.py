# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)


def one_method(request):                # no values passed via URL
    pass


def another_method(request, my_val):  # my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23


def yet_another(request, name):	        # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'


def one_more(request, id, color):   	# id would be a number, and color a string from the URL
    # given the example above, id would be 17 and color would be 'brown'
    pass


def root_method(request):
    return HttpResponse("String response from root_method")


def another_method(request):
    return redirect("/redirected_route")


def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})
