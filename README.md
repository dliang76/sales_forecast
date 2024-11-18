Store item sales forecast API

Requires: Docker

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

1. Use curl in command lines.
```bash
curl -H "Content-Type: application/json" -X POST -d '{"date":"2022-01-01","store":1,"item":2}' http://127.0.0.1:8000/predict
```

1. Use requests module in python
```bash
import requests
# get forecast
sales_forecast = requests.post(url = 'http://127.0.0.1:8000/predict', json = {'date':'2022-01-31','store':store,'item':item})
print(sales_forecast.text)

# get status
api_status = requests.get(url = 'http://127.0.0.1:8000/status')
print(api_status)
```