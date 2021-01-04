import datetime
import time

import requests
from aiocqhttp import CQHttp, Event
from apscheduler.schedulers.background import BackgroundScheduler

bot = CQHttp(api_root='http://127.0.0.1:5700')

url = 'http://127.0.0.1:5700'

def getgroup():
    res = requests.get(url+"/get_group_list").json()
    id_list =[]
    for item in res['data']:
        id_list.append(item['group_id'])
    print(id_list)
    return  id_list


# getgroup()

def sendgroupmsg(msg):
    id_list = getgroup()
    # data = {"group_id": id_list[1], "message": msg, "auto_escape": False}
    # res = requests.get(url + "/send_group_msg", params=data).json()
    # print(res)
    for id in id_list:
        data ={"group_id":id,"message":msg,"auto_escape":False}
        time.sleep(3)
        res = requests.post(url+"/send_group_msg",params=data).json()
        print(res)


def yewu():
    sendgroupmsg("小程序公众号定制开发，影视系统小说cms搭建，刷流水软件，爬虫开发，需要的朋友dd，价格非常美丽，带演示，需要的老板dd~")

def task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(yewu, 'interval',  next_run_time=datetime.datetime.now(), hours=2,
                      id="666")  # 每分钟20秒的时候跑一次
    scheduler.start()
    # 定时器 每隔2个小时跑一趟

task()
input()