from django.shortcuts import render

from .models import Subject

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
    t = '<td id="class">{}</td>\n<td id="details">{}</td>\n<td id="demand">{}</td>'

    s = filter(lambda x: x.slots > 0, Subject.objects.all())
    s = [[i.subject, i.sched, float(i.demand)/float(i.slots)] for i in s]
    s.sort(key = lambda x: x[-1], reverse = True)
    s = [[i[0], i[1], "{00:.0f}%".format(i[2]*100)] for i in s]
    subjects = s

    context = { 'subjects': subjects, }
    return render(request, 'stats/demand.html', context)

