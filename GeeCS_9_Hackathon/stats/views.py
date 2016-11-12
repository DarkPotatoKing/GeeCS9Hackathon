from django.shortcuts import render

from .models import Subject

import math
from fractions import Fraction

class SubjectStats(object):

    def __init__(self, rank, slots, demand, subject, section, units, prof, sched):
        self.rank = rank
        self.slots = slots
        self.demand = demand
        self.subject = subject
        self.section = section
        self.units = units
        self.prof = prof
        self.sched = sched
        self.total_prob = 0


def index(request):
    context = {}
    return render(request, 'stats/login.html', context)

def stats(request):
    s = filter(lambda x: x.rank > 0, Subject.objects.all())
    subjects = [SubjectStats(rank=i.rank, slots=i.slots, demand=i.demand, subject=i.subject, section=i.section, units=i.units, prof=i.prof, sched=i.sched) for i in s]

    for i, val in enumerate(subjects):
        subjects[i].total_prob = float(val.slots) / float(val.demand)

        if subjects[i].total_prob  >= 1:
            subjects[i].total_prob = 1

    for i in xrange(len(subjects)):
        for j in xrange(i+1, len(subjects)):
            if (subjects[i].subject == subjects[j].subject) or (subjects[i].section == subjects[j].section):
                subjects[j].total_prob = subjects[j].total_prob * (1 - subjects[i].total_prob)

    for i, val in enumerate(subjects):
        subjects[i].total_prob *= 100
        subjects[i].total_prob = int(subjects[i].total_prob)

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

