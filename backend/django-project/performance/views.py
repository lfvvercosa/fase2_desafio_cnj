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
def varas_list(request):
    return Response('lista de varas', HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def vara_details(request, vara_id):
    return Response(f'Detalhes da vara {vara_id}', HTTP_200_OK)
    # vara = Vara.objects.get(id=vara_id)
    # res = VaraSerializer(vara).data
    # return Response(res, HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def best_varas_on_step(request):
    step_id = request.GET.get('step_id', None)
    amount_of_varas = request.GET.get('amount_of_varas', None)
    res = {
        'step_id': step_id,
        'amount_of_varas': amount_of_varas
    }
    return Response(res, HTTP_200_OK)


# Etapas
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def best_steps(request):
    vara_id = request.GET.get('vara_id', None)
    amount_of_steps = request.GET.get('amount_of_steps', None)
    res = {
        'vara_id': vara_id,
        'amount_of_steps': amount_of_steps
    }
    return Response(res, HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def worst_steps(request):
    vara_id = request.GET.get('vara_id', None)
    amount_of_steps = request.GET.get('amount_of_steps', None)
    res = {
        'vara_id': vara_id,
        'amount_of_steps': amount_of_steps
    }
    return Response(res, HTTP_200_OK)


# Processos
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def best_varas(request):
    step_id = request.GET.get('step_id', None)
    amount_of_varas = request.GET.get('amount_of_varas', None)
    res = {
        'step_id': step_id,
        'amount_of_varas': amount_of_varas
    }
    return Response(res, HTTP_200_OK)


# Comentarios
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def comments_list(request):
    return Response('Lista comentarios', HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def comment(request, comment_id):
    return Response(f'Detalhes do comentario {comment_id}', HTTP_200_OK)
