FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN python ./download
CMD gunicorn djangoBoilerplate.wsgi:application --bind 0.0.0.0:8000