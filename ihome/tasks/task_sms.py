from celery import Celery
from ihome.Lib.yuntongxun.sms import CCP
from ihome.tasks.main import app
# 定义celery对象

@app.tasks
def send_sms(to, datas, temp_id):
    '''发送短信的异步任务'''
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)

