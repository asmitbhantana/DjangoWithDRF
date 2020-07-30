from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Info
from .serializers import InfoSerailizers, InfoModelSerializers
from rest_framework import status


class InfoClassBasedView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Info.objects.all()
        serializer = InfoModelSerializers(instance=qs, many=True)
        # serializer = InfoSerailizers(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        context = {
            'test': 'THis is just testing if context data can be sent to the serializer or not! haha'
        }
        serializer = InfoModelSerializers(data=request.data, context=context)
        # serializer = InfoSerailizers(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'ok posted'}, status=status.HTTP_201_CREATED)
