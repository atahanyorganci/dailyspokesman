#!/bin/sh
celery -A newsapp.celery beat -l info
