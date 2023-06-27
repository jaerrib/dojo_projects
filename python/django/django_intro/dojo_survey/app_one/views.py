from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")
    # if request.method == "POST":
    #     val_from_field_one = request.POST["one"]
    #     val_from_field_two = request.POST["two"]


def result(request):
    context = {
        "name": request.POST["name"],
        "location": request.POST["location"],
        "language": request.POST["language"],
        "comments": request.POST["comments"],
    }
    return render(request, "result.html", context)
