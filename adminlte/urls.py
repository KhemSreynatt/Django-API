from django.urls import path

from . import views

urlpatterns = [
    path('', views.Master, name='Master'),
    # path('index',views.index, name="INDEX")
]