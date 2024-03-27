from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from utils.redis_pool import POOL

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

import redis
import psutil
import time
import json


# 后台用法
@staff_member_required
def site_manage(request):
    conn = redis.StrictRedis(connection_pool=POOL)

    back_data = {
        'slogan1': conn.hget('HOME_PAGE:slogan:1', 'slogan'),
        'slogan2': conn.hget('HOME_PAGE:slogan:2', 'slogan'),
        'intro': conn.get('intro'),
    }
    return TemplateResponse(
        request, 'admin/site-manage.html', back_data
    )


# 定时任务
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@register_job(scheduler, 'interval', seconds=60, replace_existing=True)
def resource_statistics_job():
    # 计算服务器资源存入redis，供前端可视化
    sent_before = psutil.net_io_counters().bytes_sent
    recv_before = psutil.net_io_counters().bytes_recv
    time.sleep(10)
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    sent = ((sent_now - sent_before) / 1024) * 8 / 1024
    recv = ((recv_now - recv_before) / 1024) * 8 / 1024

    disk_io_before = psutil.disk_io_counters()
    time.sleep(10)
    disk_io_after = psutil.disk_io_counters()

    read_bytes = (disk_io_after.read_bytes - disk_io_before.read_bytes) / 1024
    write_bytes = (disk_io_after.write_bytes - disk_io_before.write_bytes) / 1024

    # 磁盘读写：KB/s，带宽：Mb/s
    server_resource = json.dumps({
        'total_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'simple_time': time.strftime("%H:%M", time.localtime()),
        'cpu': psutil.cpu_percent(),
        'memory': psutil.virtual_memory().percent,
        'disk_io_read': "{0}".format("%.3f" % read_bytes),
        'disk_io_write': "{0}".format("%.3f" % write_bytes),
        'net_io_sent': "{0}".format("%.3f" % sent),
        'net_io_recv': "{0}".format("%.3f" % recv)
    })

    conn = redis.StrictRedis(connection_pool=POOL)
    if conn.llen('server_resource') > 59:
        conn.rpop('server_resource')
    conn.lpush('server_resource', server_resource)


register_events(scheduler)
scheduler.start()
