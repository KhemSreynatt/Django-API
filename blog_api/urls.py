# from django.urls import path
from .views import PostList
from rest_framework.routers import DefaultRouter

app_name='blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns= router.urls

# urlpatterns =[
#     path('post/<int:pk>/', PostDetail.as_view(),name='detailcreate'),
#     path('post/',PostList.as_view(),name='listcreate')
# ]