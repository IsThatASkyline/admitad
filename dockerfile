FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000
