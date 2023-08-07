from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('Games/',views.Games),
    path('contact/',views.contact),
    path('gallery/',views.gallery),
    path('community/',views.community),
    path('news/',views.news),
    path('',views.index),
    path('login/',views.login),
    path('viewnews/',views.viewnews),
    path('details/',views.ndetails),
    path('vdetail/',views.vdetail),
    path('about/',views.about)




]

