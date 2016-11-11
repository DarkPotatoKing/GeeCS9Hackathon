from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stats$', views.stats, name='stats'),
    url(r'^recommend$', views.recommend, name='recommend'),
    url(r'^demand$', views.demand, name='demand'),
]
