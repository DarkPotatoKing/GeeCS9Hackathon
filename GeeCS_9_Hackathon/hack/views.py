from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")

def sched(request):
    return HttpResponse("Hello, world. You're at the sched.")

def recommend(request):
    return HttpResponse("Hello, world. You're at the recommend.")

def demand(request):
    return HttpResponse("Hello, world. You're at the demand.")
