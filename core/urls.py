from django.urls import path,include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index' ),
     path('home',views.index,name='index' ),
    path('about',views.about,name='about' ),
    path('contact',views.contact,name='contact' ),
      path('success',views.success,name='success' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)