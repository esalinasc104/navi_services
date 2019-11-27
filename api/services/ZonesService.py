import json

from django.http import JsonResponse
from api.models import Zones, CoordinateZone
from api.services.BaseService import BaseService


class ZonesService(BaseService):
    def query_zone_data(self, request):
        parameters = json.loads(request.body)
        resultset = Zones.objects.filter(name__contains=str(parameters.get("filter")).upper())
        json_result = [ob.as_json() for ob in resultset]
        return super().json_response(json_result)

    def query_zone_coordiantes(self, request):
        parameters = json.loads(request.body)
        resultset = Zones.objects.filter(name__contains=str(parameters.get("filter")).upper())
        json_result = [ob.as_json() for ob in resultset]
        return JsonResponse({"data": json_result})

    def update_coordinates(self, request, zone_id):
        zone = Zones.objects.get(_id=zone_id);
        coordinates = json.loads(request.body)
        zone.coordinates = [CoordinateZone(longitude=c.get('lng'), latitude=c.get('lat')) for c in coordinates]
        zone.save()
        return super().json_response(zone.as_json(), 0);
