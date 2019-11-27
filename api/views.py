from django.http import JsonResponse

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.services.ReportService import ReportService
from api.services.ZonesService import ZonesService

zones_services = ZonesService()
report_service = ReportService()


def index(request):
    return JsonResponse({"message": "Welcome to Navi API"})


@csrf_exempt
def query(request):
    return zones_services.query_zone_data(request)


@csrf_exempt
def save_report(request):
    return report_service.save_report(request)


@csrf_exempt
def get_reports(request):
    return report_service.get_report_per_zone(request)


@csrf_exempt
def save_coordinates(request, zone_id):
    return zones_services.update_coordinates(request, zone_id)
