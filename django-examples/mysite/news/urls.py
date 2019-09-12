from django.urls import path
from django.views.generic import ListView, DetailView 
from news.models import *

urlpatterns = [
    
    path('', 
        ListView.as_view(queryset=Articles.objects.all().orderby('-date')[:20]), 
        template_name='news/posts.html' ),
    
]