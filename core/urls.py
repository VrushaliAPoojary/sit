from django.urls import path,include
from core import views


urlpatterns = [
    path('',views.index,name='index' ),
     path('home',views.index,name='index' ),
    path('about',views.about,name='about' ),
    path('contact',views.contact,name='contact' ),
]
