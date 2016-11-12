from django.shortcuts import render

from .models import Subject

def index(request):
    context = {}
    return render(request, 'stats/index.html', context)

def stats(request):
    subjects = filter(lambda x: x.rank > 0, Subject.objects.all())
    context = { 'subjects': subjects }
    return render(request, 'stats/stats.html', context)

def recommend(request):
    context = {}
    return render(request, 'stats/recommend.html', context)

def demand(request):
    s = filter(lambda x: x.slots > 0, Subject.objects.all())
    s = [[float(i.demand)/float(i.slots), i.demand, i.slots, i.subject] for i in s]
    s.sort(key = lambda x: x[0], reverse = True)
    subjects = ['{} {}/{} {}'.format(i[0], i[1], i[2], i[3]) for  i in  s]

    context = { 'subjects': subjects, }
    return render(request, 'stats/demand.html', context)

