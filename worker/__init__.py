from decouple import config
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from newsapp import create_app
from newsapp.scraper.tasks import update_news

flask_app = create_app()
flask_app.app_context().push()

REDIS_URL = config('REDIS_TLS_URL', default=None)
if REDIS_URL is None:
    REDIS_URL = config('REDIS_URL')
UPDATE_FREQUENCY = config('UPDATE_FREQUENCY', cast=float)

app = Celery('tasks')
app.conf.update(broker_url=REDIS_URL, result_backend=REDIS_URL)


@app.task
def update(category: str):
    logger = get_task_logger(__name__)
    with flask_app.app_context():
        count = update_news(category, logger=logger)
    return count


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    for category in flask_app.config['CATEGORIES']:
        sender.add_periodic_task(UPDATE_FREQUENCY,
                                 update.s(category),
                                 name=f'Update {category}')
