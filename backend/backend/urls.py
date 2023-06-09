"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import FoodList , FoodDetails, UserList, UserDetails, MessageList, MessageDetails, RatingList, RatingDetails, CommentList, CommentDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/food', FoodList.as_view()),
    path('api/food/<str:pk>', FoodDetails.as_view()),
    path('api/user', UserList.as_view()),
    path('api/user/<str:pk>', UserDetails.as_view()),
    path('api/message', MessageList.as_view()),
    path('api/message/<str:pk>', MessageDetails.as_view()),
    path('api/rating', RatingList.as_view()),
    path('api/rating/<str:pk>', RatingDetails.as_view()),
    path('api/comment', CommentList.as_view()),
    path('api/comment/<str:pk>', CommentDetails.as_view()),
]
