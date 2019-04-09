from django.urls import path
from django.conf.urls import url
from. import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'search/', views.book_search, name='book_search'),
    url(r'about/', views.about, name='about'),
    url(r'^book/detail$', views.book_detail, name='book_detail'),
    url(r'^statistics/', views.statistics, name='statistics')
]
