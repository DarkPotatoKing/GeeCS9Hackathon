from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'sched', views.sched, name='sched'),
    url(r'recommend', views.recommend, name='recommend'),
    url(r'demand', views.demand, name='demand'),

]
