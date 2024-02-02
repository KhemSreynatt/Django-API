from django.shortcuts import render
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import  BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework import viewsets,generics,filters,permissions ,status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser



# class PostUserWirtePermission(BasePermission):
#     messages='Editing post is restricted to the author only.'
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.author == request.user
# class PostList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
 
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, id=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Post.objects.all()
class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)



class PostListDetailfilter(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']
# Post Admin

class CreatePost(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes= [permissions.IsAuthenticated]
    queryset= Post.objects.all()
    serializer_class=PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes= [permissions.IsAuthenticated]
    queryset= Post.objects.all()
    serializer_class= PostSerializer

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset= Post.objects.all()
    serializer_class= PostSerializer






""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""