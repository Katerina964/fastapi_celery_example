from .celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# app.conf.beat_schedule = {
#     'add-every-5-seconds': {
#         'task': 'add',
#         'schedule': 5.0,
#         'args': (30, 3),

#     },
#     'mul-every-5-seconds': {
#         'task': 'tasks.mul',
#         'schedule': 5.0,
#         'args': (30, 3),
#     },
#     'test-every-5-seconds': {
#         'task': 'tasks.test',
#         'schedule': 5.0,
#         'args': ("HELLO")
#     }

# }

@app.task
def add(x, y):
    s = x + y
    logger.info(f'RESULT: {s}')
    return x + y


@app.task
def mul(x, y):
    s = x * y
    logger.info(f'RESULT: {s}')
    return x * y


@app.task
def test(a):
    logger.info(f'RESULT: {a}')
    return a