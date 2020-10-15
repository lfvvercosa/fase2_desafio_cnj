from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Vara, StepConfiguration, Comments, Steps
from .serializers import VaraSerializer, VaraListSerializer, StepConfigurationSerializer, CommentsSerializer, StepsSerializer
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
    try:
        vara_list = Vara.objects.all()
        res = [VaraListSerializer(vr).data for vr in vara_list]
        return Response(res, HTTP_200_OK)
    except Vara.DoesNotExist as e:
        return Response(str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def vara_details(request, vara_id):
    try:
        vara = Vara.objects.get(vara_id=vara_id)
        res = VaraSerializer(vara).data
        return Response(res, HTTP_200_OK)
    except Vara.DoesNotExist as e:
        return Response(str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)

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
    try:
        comm_list = Comments.objects.all()
        res = [CommentsSerializer(cl).data for cl in comm_list]
        return Response(res, HTTP_200_OK)
    except Comments.DoesNotExist as e:
        return Response(str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def comment(request, comment_id):
    try:
        comm = Comments.objects.get(comment_id=comment_id)
        res = CommentsSerializer(comm).data
        return Response(res, HTTP_200_OK)
    except Comments.DoesNotExist as e:
        return Response(str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)
