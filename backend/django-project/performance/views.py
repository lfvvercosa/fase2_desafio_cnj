from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Group, Vara, StepConfiguration, Comments, Steps
from .serializers import GroupSerializer, VaraSerializer, VaraDetailsSerializer, VaraListSerializer,\
    StepConfigurationSerializer, CommentsSerializer, StepsSerializer
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
        vara_res = VaraDetailsSerializer(vara).data
        group_id = vara_res['group_id']
        group = Group.objects.get(group_id=group_id)
        group_res = GroupSerializer(group).data
        vara_res['group'] = group_res
        vara_res.pop('group_id')
        return Response(vara_res, HTTP_200_OK)
    except Vara.DoesNotExist as e:
        return Response(str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def best_varas_on_step(request):
    try:
        step_id = request.GET.get('step_id', None)
        amount_of_varas = int(request.GET.get('amount_of_varas', 10))
        step_objects = Steps.objects.filter(step_id=step_id).order_by('med_time')[:amount_of_varas]
        res_steps = []
        for step in step_objects.all():
            step_dict = StepsSerializer(step).data
            res_dict = {
                'vara_id': step_dict['vara_id'],
                'med_time': step_dict['med_time']
            }
            # Get vara info
            vara_obj = Vara.objects.get(vara_id=res_dict['vara_id'])
            vara = VaraSerializer(vara_obj).data
            res_dict['vara_name'] = vara['name']
            # Get comment info
            comment_obj = Comments.objects.get(comment_id=step_dict['comment_id'])
            comment = CommentsSerializer(comment_obj).data
            res_dict['comment'] = comment['comment']
            res_steps.append(res_dict)
        return Response(res_steps, HTTP_200_OK)
    except Steps.DoesNotExist as e:
        return Response('Error getting steps. ' + str(e), HTTP_404_NOT_FOUND)
    except Vara.DoesNotExist as e:
        return Response('Error getting vara. ' + str(e), HTTP_404_NOT_FOUND)
    except Comments.DoesNotExist as e:
        return Response('Error getting comment. ' + str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)


# Etapas
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def best_steps(request):
    try:
        vara_id = request.GET.get('vara_id', None)
        amount_of_steps = int(request.GET.get('amount_of_steps', 10))
        step_objects = Steps.objects.filter(vara_id=vara_id).order_by('med_time')[:amount_of_steps]
        res_steps = []
        for step in step_objects.all():
            step_dict = StepsSerializer(step).data
            res_dict = {
                'step_id': step_dict['step_id'],
                'med_time': step_dict['med_time'],
                'frequency': step_dict['frequency']
            }
            # Get step info
            step_config_obj = StepConfiguration.objects.get(step_id=res_dict['step_id'])
            step_config = StepConfigurationSerializer(step_config_obj).data
            res_dict['origin'] = step_config['origin']
            res_dict['destination'] = step_config['destination']
            res_steps.append(res_dict)
        return Response(res_steps, HTTP_200_OK)
    except Steps.DoesNotExist as e:
        return Response('Error getting steps. ' + str(e), HTTP_404_NOT_FOUND)
    except StepConfiguration.DoesNotExist as e:
        return Response('Error getting step configuration. ' + str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def worst_steps(request):
    try:
        vara_id = request.GET.get('vara_id', None)
        amount_of_steps = int(request.GET.get('amount_of_steps', 10))
        step_objects = Steps.objects.filter(vara_id=vara_id).order_by('-med_time')[:amount_of_steps]
        res_steps = []
        for step in step_objects.all():
            step_dict = StepsSerializer(step).data
            res_dict = {
                'step_id': step_dict['step_id'],
                'med_time': step_dict['med_time'],
                'frequency': step_dict['frequency']
            }
            # Get step info
            step_config_obj = StepConfiguration.objects.get(step_id=res_dict['step_id'])
            step_config = StepConfigurationSerializer(step_config_obj).data
            res_dict['origin'] = step_config['origin']
            res_dict['destination'] = step_config['destination']
            res_steps.append(res_dict)
        return Response(res_steps, HTTP_200_OK)
    except Steps.DoesNotExist as e:
        return Response('Error getting steps. ' + str(e), HTTP_404_NOT_FOUND)
    except StepConfiguration.DoesNotExist as e:
        return Response('Error getting step configuration. ' + str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)


# Processos
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def best_varas(request):
    try:
        vara_id = request.GET.get('vara_id', None)
        amount_of_varas = int(request.GET.get('amount_of_varas', 10))
        all_vara_obj_list = Vara.objects.order_by('days_finish_process')

        first_objs = all_vara_obj_list[:max(amount_of_varas - 5, 1)]
        focused_vara_index = list(all_vara_obj_list.all()).index(Vara.objects.get(vara_id=vara_id))
        min_index_to_get = max(0, focused_vara_index-2)
        max_index_to_get = focused_vara_index + 3
        last_objs = all_vara_obj_list[min_index_to_get:max_index_to_get]
        objs = first_objs.union(last_objs).distinct()
        if amount_of_varas > len(objs):
            objs = objs.union(all_vara_obj_list[:amount_of_varas]).distinct()

        objs = objs.order_by('days_finish_process')

        res_list = []
        for vara_obj in objs.all():
            vara = VaraSerializer(vara_obj).data
            res_list.append(vara)
        return Response(res_list, HTTP_200_OK)
    except Vara.DoesNotExist as e:
        return Response('Error getting vara. ' + str(e), HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), HTTP_400_BAD_REQUEST)


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
