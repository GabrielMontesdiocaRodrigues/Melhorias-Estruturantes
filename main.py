from fastapi import FastAPI
from celery import Celery

app = FastAPI()

scraper_app = Celery('queue',
                     broker='amqp://user:password@rabbitmq:5672',
                     backend='')


@app.post('/scrape')
def resquest_task(in_cnpj: str):
    r = scraper_app.send_task('worker.scrape',
                              kwargs={'inCnpj': in_cnpj})
    return r.id


@app.get('/results/{task_id}:')
def task_result(task_id):
    result = scraper_app.AsyncResult(task_id)
    return "Result of the Task " + str(result)
