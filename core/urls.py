from django.contrib import admin
from django.urls import path, include
# from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from blog.admin import blogbsite
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/master',include('adminlte.urls')),
    path('apps/', include('apps.urls')),
    # path("", include('admin_argon.urls')),
     # Project URLs

    path('admin/', admin.site.urls),
    path('', include('blog.urls',namespace='blog')),

    # Blog_API Application
    path('api/',include('blog_api.urls',namespace='blog_api')),

    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    path('api/profiles', include('profiles.urls', namespace='profiles')),
    # API Token Management
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

] 
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
