import time
import paramiko
import math
from threading import Timer
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from monitor.models import Project1
datatime = time.strftime("%Y-%m-%d")
project=[]
path=[]
size=[]
ip = "114.115.132.122"
port = 22
user = "guixin2"
password = "123456"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, user, password, timeout=10)
cat = "cat /home/guixin2/python/project_tongji/tongji"
stdin, stdout, stderr = ssh.exec_command(cat)
result = stdout.readlines()
list1=[]
for line in result:
    line = line.split(',')
    project.append(line[0])
    path.append(line[1])
    size.append(line[2])
# print(len(project))
list2=[]
for line in project:
    line = line.split('{')
    # line = line.split('{')
    # print(line[1])
    line1 = line[1].split('\\')
    line2 = line1[0]
    line3 = line1[1]
    line3 = line3.split('"')
    list2.append(line3[1])
list3=[]
for line in path:
    line=line.split(':')
    line1=line[1]
    line1=line1.split('\\')
    line2=line1[1]
    line2=line2.split('"')
    list3.append(line2[1])
list4=[]
# print(len(size))
for line in size:
    line = line.split('"')
    line1 = line[3]
    line1=int(line1)
    list4.append(line1)
# print(list4)
for i in range(len(list2)):
    Project1.objects.create(project=list2[i], path=list3[i], size=list4[i], datatime=datatime,
                               cluster='huaweicloud')
