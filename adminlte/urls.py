from django.urls import path

from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    # path('index',views.index, name="INDEX")
]