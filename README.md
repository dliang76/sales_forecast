<h3><ins>Instruction for store item sales forecast API<ins></h3>

Requirement: Docker

Install and start the API:
```bash
# Clone the repo
git clone https://github.com/dliang76/sales_forecast.git

cd sales_forecast

# build docker image and run
docker build -t sales_forecast .
docker run -p 8000:8000 sales_forecast
```

How to run locally:

1. Use web browsers for interactive sessions. Go to http://127.0.0.1:8000/docs.

2. Use `curl` in command lines.
```bash
# get forecast for a specific store and item (change -d argument for different inputs)
curl -X POST -d '{"date":"2022-01-01","store":1,"item":2}' http://127.0.0.1:8000/predict

# check status
curl -X GET http://127.0.0.1:8000/status
```

3. Use `requests` module in python
```bash
import requests
# get forecast for a specific store and item  (change json argument for different inputs)
sales_forecast = requests.post(url = 'http://127.0.0.1:8000/predict', json = {'date':'2022-01-31','store':store,'item':item})
print(sales_forecast.text)

# check API status
api_status = requests.get(url = 'http://127.0.0.1:8000/status')
print(api_status)
```

<h3><ins>Instruction for model training<ins></h3>

The notebook for training the model is in the same `sales_forecast` repo. The location is `sales_forecast/notebook/model_training.ipynb`.

How to run the notebook:

1. In the `sales_forecast` directory,
    ```bash
    # install required python packages
    pip install -r requirements.txt
    ```
1. Download `train.csv` from https://www.kaggle.com/c/demand-forecasting-kernels-only/data and copy/move it into `sales_forecast/ml/data` folder

1. Run the notebook

