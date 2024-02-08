from celery import Celery

app = Celery('celery_service',
            #  broker='pyamqp://rabbitmq_user:rabbitmq_password@rabbitmq:5672//',
             broker='redis://redis:6379/0',
             include=['celery_service.tasks'])

app.conf.update(
    result_expires=3600,
)
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'celery_service.tasks.add',
        'schedule': 15000.0,
        'args': (30, 3),
        'options': {'queue':'myadd'}
    },
}
task_routes = {
    'celery_service.tasks.mul': 'mymul',
    'celery_service.tasks.add': 'myadd',}
# app.autodiscover_tasks(['celery_service.tasks'])
app.control.add_consumer('myadd', reply=True)

if __name__ == '__main__':
    app.start()