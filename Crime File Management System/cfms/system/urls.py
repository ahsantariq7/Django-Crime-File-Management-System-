from django.contrib import admin
from django.urls import path
from system import views
from django.contrib.auth import views as auth_views
from . import views
from .views import AddMissingPerson,AddMissingPersonForm,CreatePostView,ShowMostWantedPerson,CreatePostView2
 

urlpatterns = [
    path("",views.index, name="index"),
    path("expression",views.expression, name='expressionvalue'),
    path("service",views.service, name='service'),
    path("base",views.base, name="base"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('success/', views.home, name='success'),
    path('about/', views.about, name='about'),
    path("miss/", AddMissingPerson.as_view(),name='miss'),
    path("post/", CreatePostView.as_view(), name="post"),
    path("most/", ShowMostWantedPerson.as_view(),name='most'),
    path("post2/", CreatePostView2.as_view(), name="post2"),
    path("firwrite",views.firwrite, name='firwrite'),
    path("crime1",views.crime1, name='crime1'),
    path("addcomplaint",views.addcomplaint, name='addcomplaint'),
    path("contact",views.contact, name='contact'),

  
]
