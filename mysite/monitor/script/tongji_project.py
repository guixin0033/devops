import time
import paramiko
import math
import re
import os
from collections import Counter
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from monitor.models import tongji
ip = "114.115.132.122"
port = 22
user = "guixin2"
password = "123456"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, user, password, timeout=10)
tongji_project = "cat /home/guixin2/python/project_tongji/tongji_project"
stdin, stdout, stderr = ssh.exec_command(tongji_project)
meta_project_result = stdout.readlines()
tongji_total =  "cat /home/guixin2/python/dir_tongji/tongji"
stdin, stdout, stderr = ssh.exec_command(tongji_total)
tongji_total_result = stdout.readlines()
ssh.close()
list10=[]
list20=[]
for line in meta_project_result:
    line=line.split('[')
    for line1 in line:
        if len(line1) > 1:
            list10.append(line1)
for line in list10:
    line=line.split(']')
    for line1 in line:
        if len(line1) > 2:
            list20.append(line1)
list30=[]
list40=[]
for line in list20:
    line=line.split('"')
    line1=line[2]
    line2=line[3]
    list30.append(line1)
    list40.append(line2)
list50=[]
list60=[]
for line in list30:
    line=line.split('\\')
    line1=line[0]
    line1=line1.split('_')
    line2=line1[0]
    line2=line2.upper()
    # print(line2)
    list50.append(line2)
for line in list40:
    line=line.split(':')
    line1=line[1]
    line1=line1.split('}')
    line2=line1[0]
    line2=int(line2)
    list60.append(line2)
list70=zip(list50,list60)
dict1=dict(list70)
# print(dict1)
list1=[]
list2=[]
for line in tongji_total_result:
    line=line.split('[')
    for line1 in line:
        if len(line1) > 1:
            list1.append(line1)
list3=[]
for line in list1:
    if 'project' in line:
        if 'Rand' not in line:
            # print(line)
            line=line.split(',')
            line1=line[2]
            line2=line[0]
            list2.append(line1)
            list3.append(line2)
list4=[]
for line in list2:
    line=line.split(']')
    line1=line[0]
    line1=int(line1)
    line2=line1/math.pow(1023,3)
    line2=round(line2)
    list4.append(line2)
list5=[]
for line in list3:
    line=line.split('\\')
    line1=line[1]
    line1=line1.split('/')
    line2=line1[2]
    list5.append(line2)
list6=zip(list5,list4)
dict2=dict(list6)
# print(dict2)
dict3=dict(Counter(dict2)-Counter(dict1))
# print(dict3)
for line in dict3.keys():
    tongji.objects.create(pro=line,type='project',size=dict1[line])
    tongji.objects.create(pro=line,type='unkown',size=dict3[line])
