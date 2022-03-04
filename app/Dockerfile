FROM python:3.9

COPY ./requirements.txt .
RUN pip install -r requirements.txt 

ENV PYTHONPATH=/app

WORKDIR /app

COPY . .

ENTRYPOINT [ "sh", "docker-entrypoint.sh" ]
