from fastapi import FastAPI
from celery import Celery
from worker.config import Environment
import redis
import json

app = FastAPI()

scraper_app = Celery('sintegra-go-scrap-request-queue',
                     broker='amqp://user:password@rabbitmq:5672')

client = redis.Redis(host=Environment().REDIS_HOST,
                     port=6379, db=0, password="1q2w3e4r")


@app.post('/scrape')
async def resquest_task(in_cnpj: str):
    task_signature = scraper_app.signature('sintegra-go-scrape', queue='sintegra-go-scrap-request-queue',
                                           kwargs={'in_Cnpj': in_cnpj})
    async_result = task_signature.apply_async()
    task_id = async_result.id
    return task_id


@app.get('/results/{task_id}:')
async def task_result(task_id):
    retrieved_data = client.get(task_id)
    if retrieved_data:
        retrieved_data = json.loads(retrieved_data)
        return retrieved_data
    return {'message': 'not found task'}
