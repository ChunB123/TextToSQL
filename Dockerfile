FROM python:3.10

COPY . /TextToSQL

WORKDIR /TextToSQL/flask_app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=True
ENV DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

CMD ["flask", "run"]