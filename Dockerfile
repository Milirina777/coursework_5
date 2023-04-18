FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=wsgi.py

CMD gunicorn wsgi:app -b 0.0.0.0:80 -w 3