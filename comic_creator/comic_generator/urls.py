from django.urls import path
from .views import create_comic_panel

urlpatterns = [
    path('', create_comic_panel, name='create_comic_panel'),
]
