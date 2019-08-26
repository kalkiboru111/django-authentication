from django.shortcuts import render

# REturn the index.html file
def index(request):
    return render(request, "index.html")