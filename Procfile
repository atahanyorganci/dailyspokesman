web: gunicorn "newsapp:create_app()"
scrapper: REMAP_SIGTERM=SIGQUIT celery --app worker worker --beat -l INFO
