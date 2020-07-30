from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Info
from .serializers import InfoModelSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permission import IsStaffUser


class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializers
    queryset = Info.objects.all()
    # permission_classes = [IsStaffUser]
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsStaffUser]
        elif self.action == 'list':
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

# class InfoModelViewSet(ReadOnlyModelViewSet):
#     serializer_class = InfoModelSerializers
#     queryset = Info.objects.all()
