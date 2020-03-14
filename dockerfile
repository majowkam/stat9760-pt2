FROM python:3.7

WORKDIR /app

RUN mkdir /app/out

COPY . .

RUN pip install -r requirements.txt
