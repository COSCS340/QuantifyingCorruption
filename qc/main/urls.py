from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^results/$', views.results, name='results'),
    path('search/', views.search, name='search'),
    path('search', views.search, name='search'),
    path('legislator/<int:legislator_id>', views.legislator, name='legislator'),
    path('hello/', views.helloworld, name='helloworld'),
    path('about/', views.about, name='about'),
    path('', views.splash, name='splash'),
]
