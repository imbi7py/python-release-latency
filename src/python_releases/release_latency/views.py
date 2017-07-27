from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, "release_latency/index.html")
