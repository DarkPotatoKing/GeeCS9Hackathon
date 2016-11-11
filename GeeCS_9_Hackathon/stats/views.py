from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'stats/index.html', context)

def stats(request):
    context = {}
    return render(request, 'stats/stats.html', context)

def recommend(request):
    context = {}
    return render(request, 'stats/recommend.html', context)

def demand(request):
    context = {}
    return render(request, 'stats/demand.html', context)

