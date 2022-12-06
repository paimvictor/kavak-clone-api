from logging import getLogger

from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from kovak_api.carshop.models import Car
from kovak_api.carshop.serializers import CarSerializer

LOGGER = getLogger(__name__)


class CarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ """
        if request.query_params:
            cars = Car.objects.filter(**request.query_params.dict())
        else:
            cars = Car.objects.all()

        if not cars:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = CarSerializer(cars, many=True)
        return Response(data.data)

    def post(self, request, *args, **kwargs):
        """
        Create the Car with given data
        """
        car = CarSerializer(data=request.data)

        if car.is_valid():
            car.save()
            return Response(car.data, status=status.HTTP_201_CREATED)

        LOGGER.debug(car.errors)
        return Response(car.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=request.data.get("id"))
        data = CarSerializer(instance=car, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        """
        Delete the Car with given id
        """
        car = get_object_or_404(Car, id=request.query_params.get("id"))
        car.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
