from django.urls import path
from . import views
from django.conf import settings  # Ensure this import is present
from django.conf.urls.static import static  # Ensure this import is present

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.index, name='songs'),
    # path('songs/', views.all_songs, name='all_songs'),
    path('hindi/', views.hindi_songs, name='hindi'),
    path('kannada/', views.kannada_songs, name='kannada'),
    path('english/', views.english_songs, name='english'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
