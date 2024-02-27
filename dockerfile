FROM python:3.9
WORKDIR /fastapi_celery_example
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /fastapi_celery_example