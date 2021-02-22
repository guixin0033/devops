import paramiko
import time
import math
import os
from threading import Timer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from monitor.models import info
ip = "114.115.132.122"
port = 22
user = "guixin2"
password = "123456"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, user, password, timeout=10)
cp = "cat /home/guixin2/info.txt"
stdin, stdout, stderr = ssh.exec_command(cp)
result = stdout.readlines()
total = []
for line in result:
    line = line.strip()
    line = line.split(',')
    total.append(line)
hostname = []
cpu = []
mem = []
disk = []
datatime = []
cluster = []
for line in total:
    line1 = line[1]
    line1 = line1.split(':')[1]
    line1 = eval(line1)
    hostname.append(line1)
    line2 = line[2]
    line2 = line2.split(':')[1]
    line2 = float(line2)
    line2 = round(line2)
    mem.append(line2)
    line3 = line[3]
    line3 = line3.split(':')[1]
    line3 = float(line3)
    line3 = round(line3)
    cpu.append(line3)
    line4 = line[4]
    line4 = line4.split(':')[1]
    line4 = float(line4)
    line4 = round(line4)
    disk.append(line4)
    line0 = line[0]
    line0 = line0.split(':')[1]
    line0 = eval(line0)
    datatime.append(line0)
    line5 = line[5]
    line5 = line5.split(':')[1]
    line5 = line5.split('}')
    line5 = line5[0]
    line5 = eval(line5)
    cluster.append(line5)
for i in range(len(hostname)):
    info.objects.get_or_create(hostname=hostname[i],cpu=cpu[i],mem=mem[i],disk=disk[i],datatime=datatime[i],cluster=cluster[i])


