import os
from django.apps import AppConfig
from django.conf import settings
import lightgbm as lgb

class ForecastAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forecastApp'

    # load model
    model_loc = os.path.join(settings.MODEL_DIR, 'lgbm')
    model = lgb.Booster(model_file = model_loc)