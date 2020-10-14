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


# Home
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def home(request):
    return Response('home', HTTP_200_OK)


# Varas
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def lista_varas(request):
    return Response('lista de varas', HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def detalhes_vara(request, vara_id):
    return Response(f'Detalhes da vara {vara_id}', HTTP_200_OK)
    vara = Vara.objects.get(id=vara_id)

    res = VaraSerializer(vara).data

    return Response(res, HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def melhores_varas_na_etapa(request):
    identificador = request.GET.get('identificador', None)
    numeroDeVaras = request.GET.get('numeroDeVaras', None)
    res = {
        'identificador': identificador,
        'numeroDeVaras': numeroDeVaras
    }
    return Response(res, HTTP_200_OK)


# Etapas
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def melhores_etapas(request):
    identificador = request.GET.get('identificador', None)
    numeroDeEtapas = request.GET.get('numeroDeEtapas', None)
    res = {
        'identificador': identificador,
        'numeroDeEtapas': numeroDeEtapas
    }
    return Response(res, HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def piores_etapas(request):
    identificador = request.GET.get('identificador', None)
    numeroDeEtapas = request.GET.get('numeroDeEtapas', None)
    res = {
        'identificador': identificador,
        'numeroDeEtapas': numeroDeEtapas
    }
    return Response(res, HTTP_200_OK)


# Processos
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def melhores_varas(request):
    identificador = request.GET.get('identificador', None)
    numeroDeVaras = request.GET.get('numeroDeVaras', None)
    res = {
        'identificador': identificador,
        'numeroDeVaras': numeroDeVaras
    }
    return Response(res, HTTP_200_OK)


# Comentarios
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def lista_comentarios(request):
    return Response('Lista comentarios', HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def comentario(request, identificador):
    return Response(f'Detalhes do comentario {identificador}', HTTP_200_OK)
