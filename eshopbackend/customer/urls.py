from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('userstore/', views.UserStore.as_view(),name='userstore')
]