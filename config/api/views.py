from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Barber, Service, ServiceCategory, User

from .serializers import (
    BarberSerializer,
    ServiceCategorySerializer,
    ServiceSerializer,
    UserSerializer,
)


def _not_found():
    return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


def _invalid(serializer):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return _not_found()
    return Response(UserSerializer(user).data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return _not_found()

    serializer = UserSerializer(user, data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def barbers(request):
    serializer = BarberSerializer(Barber.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def barber_detail(request, pk):
    try:
        barber = Barber.objects.get(pk=pk)
    except Barber.DoesNotExist:
        return _not_found()
    return Response(BarberSerializer(barber).data)


@api_view(['POST'])
def create_barber(request):
    serializer = BarberSerializer(data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_barber(request, pk):
    try:
        barber = Barber.objects.get(pk=pk)
    except Barber.DoesNotExist:
        return _not_found()

    serializer = BarberSerializer(barber, data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_barber(request, pk):
    try:
        barber = Barber.objects.get(pk=pk)
    except Barber.DoesNotExist:
        return _not_found()

    barber.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def service_category(request):
    serializer = ServiceCategorySerializer(ServiceCategory.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def service_category_detail(request, pk):
    try:
        service_category = ServiceCategory.objects.get(pk=pk)
    except ServiceCategory.DoesNotExist:
        return _not_found()
    return Response(ServiceCategorySerializer(service_category).data)


@api_view(['POST'])
def create_service_category(request):
    serializer = ServiceCategorySerializer(data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_service_category(request, pk):
    try:
        service_category = ServiceCategory.objects.get(pk=pk)
    except ServiceCategory.DoesNotExist:
        return _not_found()

    serializer = ServiceCategorySerializer(service_category, data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_service_category(request, pk):
    try:
        service_category = ServiceCategory.objects.get(pk=pk)
    except ServiceCategory.DoesNotExist:
        return _not_found()

    service_category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def services(request):
    serializer = ServiceSerializer(Service.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def service_detail(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return _not_found()
    return Response(ServiceSerializer(service).data)


@api_view(['POST'])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return _not_found()

    serializer = ServiceSerializer(service, data=request.data)
    if not serializer.is_valid():
        return _invalid(serializer)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return _not_found()

    service.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
