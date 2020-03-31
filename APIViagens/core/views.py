import json
from django.http import JsonResponse

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from core.models import Trip, Classification


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_trips(request):
    """
    Função que recupera ultimas 5 viagens do usuário

    :param request: none
    :return: JSONArray contendo 5 JSONs com as informações das ultimas viagens do usuário e HTTP Status 200 OK
    """

    trips = Trip.objects.all().filter(user_id = request.user)[:5]
    try:
        latest = []
        for i in range(0, len(trips)):

            singleTrip = {
                'data_inicio': trips[i].data_inicio,
                'data_fim': trips[i].data_fim,
                'classificacao': trips[i].classificacao.classificacao,
                'nota': trips[i].nota
            }
            latest.append(singleTrip)
        data = {
            "Latest Trips": latest
        }

        return JsonResponse(data)
    except:
        data = {
            "Response": "Could not find any trips!"
        }
        return JsonResponse(data, status=401)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def update_trips(request):

    """
    Função que atualiza base com avaliação de uma viagem enviada pelo usuário

    :param request: JSON contendo as informações de início e fim da viagem assim como classificação e nota da mesma
    :return: Mensagem e HTTP Status 201 Created
    """

    json_str = ((request.body).decode('utf-8'))
    json_obj = json.loads(json_str)
    nota_json = json_obj['nota']
    if (nota_json < 1 | nota_json > 5):
        data = {
            "Response": "Nota deve estar entre 1 e 5!"
        }
        return JsonResponse(data, status=400)
    data_inicio_json = json_obj['data_inicio']
    data_fim_json = json_obj['data_fim']
    classificacao_json = json_obj['classificacao']

    try:
        classificacao = Classification.objects.get(classificacao=classificacao_json)
        trip = Trip(user_id = request.user, data_inicio=data_inicio_json, data_fim=data_fim_json,classificacao=classificacao,nota=nota_json)
        trip.save()
        data = {
            "Response": "Informações da viagen salvas com sucesso"
        }
        return JsonResponse(data, status=201)
    except:
        data = {
            "Response": "Não foi possível avaliar a viagem"
        }
        return JsonResponse(data, status=400)
