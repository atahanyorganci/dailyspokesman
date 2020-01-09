#!/bin/sh
celery -A entry.celery beat -l info
