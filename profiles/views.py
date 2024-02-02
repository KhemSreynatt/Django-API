
from rest_framework import viewsets
from .serializers import PosfilesSerializer
from .models import Profile
from rest_framework.response import Response
class ProfiletList(viewsets.ReadOnlyModelViewSet):
    serializer_class = PosfilesSerializer
    queryset = Profile.objects.all()

    def list(self,request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many= True)
        data={
            "data": serializer.data
        }
        return Response(data)
