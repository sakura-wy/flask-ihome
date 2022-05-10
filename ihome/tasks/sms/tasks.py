
from ihome.tasks.task_sms import send_sms
from ihome.tasks.main import app
from ihome.Lib.yuntongxun.sms import CCP

@app.tasks
def send_template_sms(to, datas, temp_id):
    '''发送短信的异步任务'''
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)

