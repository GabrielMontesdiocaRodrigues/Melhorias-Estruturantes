from .scraper import Scraper
from celery import Celery, current_task
from .config import Environment
import redis

app = Celery('sintegra-go-scrap-request-queue',
             broker='amqp://user:password@rabbitmq:5672')

client = redis.Redis(host=Environment().REDIS_HOST,
                     port=6379, db=0, password="1q2w3e4r")


@app.task(name='sintegra-go-scrape', queue='sintegra-go-scrap-request-queue')
def scrape(in_Cnpj: str):
    task_id = current_task.request.id
    scrape = Scraper(in_Cnpj)
    response_json = scrape.main()
    client.set(task_id, response_json, 300)
