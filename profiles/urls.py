from django.urls import path,include
# from .views import ProfiletList
from rest_framework import routers
from profiles import views
app_name ='profiles'

router= routers.DefaultRouter()
router.register(r'profiles',views.ProfiletList)

urlpatterns=[
    path('/',include(router.urls)),
]