from django.http import JsonResponse

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.services.ZonesService import ZonesService

zones_services = ZonesService()


def index(request):
    return JsonResponse({"message": "Welcome to Navi API"})


@csrf_exempt
def query(request):
    return zones_services.query_zone_data(request)
