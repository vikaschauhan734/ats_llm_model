FROM python:3.11.8-alpine
COPY . /app
WORKDIR /app
RUN apk update && apk add poppler-utils && pip install -r requirements.txt
CMD python app.py