from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def main_view(request):
  # return HttpResponse("<h1>Welcome to Automax!</h1>")
  return render(request, "views/main.html", {"name": "Autoax"})
