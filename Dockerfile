FROM python:3.11

# set working directory
WORKDIR /app

# copy project folder to /app folder
COPY . /app

# install required packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# expose port to the host
EXPOSE 8000

# start HTTP server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sales_forecast.wsgi:application"]