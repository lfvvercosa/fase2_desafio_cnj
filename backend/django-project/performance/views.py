from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Vara
from .serializers import VaraSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, \
                                      permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, \
                                  HTTP_404_NOT_FOUND, \
                                  HTTP_200_OK
from rest_framework.permissions import AllowAny


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def view_vara(request, vara_id):
    vara = Vara.objects.get(id=vara_id)

    res = VaraSerializer(vara).data

    return Response(res, HTTP_200_OK)
