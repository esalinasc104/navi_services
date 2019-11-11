import datetime
import json

from api.models import DangerRangeZone, Zones
from api.services.BaseService import BaseService


class ReportService(BaseService):
    def save_report(self, request):
        report = json.loads(request.body)
        danger_zone = DangerRangeZone()
        danger_zone.parser_to_obj(report)
        danger_zone.save()
        return super().json_response(danger_zone.as_json())

    def get_report_per_zone(self, request):
        parameters = json.loads(request.body)
        list_reports = DangerRangeZone.objects.filter(zone___id=parameters.get("zone_id"))
        json_result = [ob.as_json() for ob in list_reports]
        return super().json_response(json_result)
