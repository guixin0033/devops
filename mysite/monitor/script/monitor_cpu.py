import psutil
import sqlite3
from datetime import datetime
import os
# db_name = '/Users/guixin/PycharmProjects/django/mysite/db.sqlite'
conn = sqlite3.connect(db_name)
c = conn.cursor()
now = datetime.now()
hostname = os.popen('hostname').read().splitlines()[0]
cpu_percent = psutil.cpu_percent()
cpu_time = datetime.strftime(now, ('%Y-%m-%d %H:%M:%S'))
sql_cpu = "insert into monitor_cpu_info(hostname,cpu_percent,cpu_time) values('%s','%s','%s')" % (
hostname, cpu_percent, cpu_time)
c.execute(sql_cpu)
conn.commit()
conn.close()
