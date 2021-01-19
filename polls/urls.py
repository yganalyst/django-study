# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:38:24 2021

@author: user
"""

from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),    
]

