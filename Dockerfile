FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV TZ="America/Sao_Paulo"
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 8000
