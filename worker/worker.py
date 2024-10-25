from scraper import Scraper
from celery import Celery

app = Celery('worker',
             broker='amqp://user:password@rabbitmq:5672',
             backend='')


@app.task()
def scrape(in_cnpj: str):
    scrape = Scraper(in_cnpj)
    scrape.main()
