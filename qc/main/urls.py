from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search', views.search, name='search'),
    path('legislator/<int:legislator_id>', views.legislator, name='legislator'),
    path('hello/', views.helloworld, name='helloworld'),
    path('', views.splash, name='splash'),
]
