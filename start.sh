#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
celery -A worker.worker worker -Q sintegra-go-scrap-request-queue --loglevel=INFO