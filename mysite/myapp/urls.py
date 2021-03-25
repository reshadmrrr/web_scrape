from .views import scrape, clear
from django.urls import path
urlpatterns = [
    path('', scrape, name='scrape' ),
    path('delete/', clear, name='clear' ),
   
]