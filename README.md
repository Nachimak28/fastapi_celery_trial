# FastAPI Celery prototype

This is an extremely basic fastapi prototype with celery task workers using redis as the message broker.

## Prerequisites:

* Redis installed in local system
* pip install -r requirements.txt

## Running locally

* FastAPI server

```sh
uvicorn main:app --host=0.0.0.0 --port=8888
```

* Celery worker

```sh
mkdir logs

celery worker --app=worker.celery --loglevel=info --logfile=logs/celery.log
```

* Flower celery monitoring server

Change port argument as needed
```sh
flower --app=worker.celery --port=8080 --broker=redis://localhost:6379/0
```



