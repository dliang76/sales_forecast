from ninja import NinjaAPI
from django.urls import path
from forecastApp.api import router as forecast_router

api = NinjaAPI()

api.add_router("", forecast_router)