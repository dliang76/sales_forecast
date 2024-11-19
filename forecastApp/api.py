from ninja import Router, Schema
from datetime import date
from typing import Dict
from http import HTTPStatus
from django.http import HttpResponse
from .apps import ForecastAppConfig
from pydantic import field_validator

router = Router()

class InputData(Schema):
    '''schema for input data'''
    date: date # datetime.date type
    store: int
    item: int

    @field_validator('store')
    def store_range_validation(cls, v):
        '''validator to make sure store inputs are between 1 and 10'''
        if v > 10 or v < 1:
            raise ValueError('store must be an integer between 1 and 10')
        return v

    @field_validator('item')
    def item_range_validation(cls, v):
        '''validator to make sure item inputs are between 1 and 50'''
        if v > 50 or v < 1:
            raise ValueError('item must be an integer between 1 and 50')
        return v


@router.get("/status")
def status(request) -> str:
    '''Endpoint for returning API running status'''

    return HttpResponse("API running...", status=HTTPStatus.OK)

@router.post("/predict")
def predict(request, input_data: InputData) -> Dict[str, float]:
    '''Endpoint for making sales prediction

        Args:
            request: http request.
            input_data: input data in json. E.g. {'date':'2022-01-01', 'store':1, 'item':2}

        Returns:
             ed sales. E.g. {'sales': 32.12}
    '''

    # get input data
    date = input_data.date # get date
    store = input_data.store # get store
    item = input_data.item # get item

    # generate features required for the model
    year = date.year # extract year
    month = date.month # extract month
    day = date.day # extract day

    model_input = [[store, item, month, day, year]] # assemble model input

    # generate sales prediction
    model = ForecastAppConfig.model
    prediction = model.predict(model_input)[0].round(2).item() # round to 2 decimal points
    response_dict = {"sales": prediction}

    return response_dict
