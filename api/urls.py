from django.http import HttpResponse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('zones/query', views.query),
    path('zones/<slug:zone_id>/coordinates', views.save_coordinates),
    path('report/create', views.save_report),
    path('report/list', views.get_reports),
]
