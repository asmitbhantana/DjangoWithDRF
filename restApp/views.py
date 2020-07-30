from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import AddTwoNumbersSerializers


# Create your views here.
@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Welcome to add to methods'})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("request.POST->", request.POST)
        print("data->", data)

        serializers = AddTwoNumbersSerializers(data=data)
        if serializers.is_valid():
            a = serializers.validated_data['a']
            b = serializers.validated_data['b']
            result = a + b
            return JsonResponse({'result': result})

        print(serializers.errors)
        return JsonResponse({'error': "some error have occured "}, status=400)


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def add_two_numbers_in_rest(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Welcome to add to methods'})

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # print("request.POST->", request.POST)
        # print("data->", data)

        data = request.data
        serializers = AddTwoNumbersSerializers(data=data)
        serializers.is_valid(raise_exception=True)
        a = serializers.validated_data['a']
        b = serializers.validated_data['b']
        result = a + b
        return Response({'result': result})


from .models import Info
from .serializers import InfoSerailizers


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def info_view(request, pk=None):
    if request.method == 'GET':
        qs = Info.objects.all()
        # result = []
        # for info in qs:
        #     serializer = InfoSerailizers(instance=info)
        #     result.append(serializer.data)
        serializer = InfoSerailizers(instance=qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InfoSerailizers(data=request.data)
        serializer.is_valid(raise_exception=True)
        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']
        # obj = Info.objects.create(name=name, address=address)
        serializer.save()
        return Response({'status': 'ok posted'})

    elif request.method == 'PUT':
        try:
            obj = Info.objects.get(id=pk)
            serializer = InfoSerailizers(data=request.data, instance=obj)
            serializer.is_valid(raise_exception=True)
            # name = serializer.validated_data['name']
            # address = serializer.validated_data['address']
            # obj.name = name
            # obj.address = address
            # obj.save()
            serializer.save()
            return Response({'status': 'ok put'})

        except Info.DoesNotExist:
            return Response({'error': "Doesn't exists"})


    elif request.method == 'PATCH':
        try:
            obj = Info.objects.get(id=pk)
            serializer = InfoSerailizers(data=request.data)
            serializer.is_valid(raise_exception=True)
            name = serializer.validated_data['name']
            address = serializer.validated_data['address']
            obj.name = name
            obj.address = address
            obj.save()
            return Response({'status': 'ok patch'})

        except Info.DoesNotExist:
            return Response({'error': "Doesn't exists"})

    return None
