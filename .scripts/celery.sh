#!/bin/sh
celery -A entry.celery worker -l info
