
from celery import Celery
# from ihome.tasks import config
app = Celery("ihome")


# app.config_from_object(Config)
app.config_from_object("ihome.tasks.config")

app.autodiscover_tasks(["ihome.tasks.sms"])