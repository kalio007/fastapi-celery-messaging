from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')
