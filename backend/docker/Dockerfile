FROM python:3.10.0-slim-buster

COPY app app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080


ENTRYPOINT [ "python",  "-m",  "app" ]