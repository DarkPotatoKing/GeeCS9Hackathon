from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'stats/index.html', context)