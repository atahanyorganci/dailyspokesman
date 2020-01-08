#!/bin/sh
celery -A newsapp.celery worker -l info
