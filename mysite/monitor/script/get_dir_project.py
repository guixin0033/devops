import paramiko
import time
import math
import os
from threading import Timer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from monitor.models import Dir
ip = "114.115.132.122"
port = 22
user = "guixin2"
password = "123456"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, user, password, timeout=10)
meta = "cat /home/guixin2/python/dir_tongji/meta"
res = "cat /home/guixin2/python/dir_tongji/res"
rna = "cat /home/guixin2/python/dir_tongji/rna"
dna = "cat /home/guixin2/python/dir_tongji/dna"
hic = "cat /home/guixin2/python/dir_tongji/3d"
stdin, stdout, stderr = ssh.exec_command(meta)
result_meta = stdout.readlines()
stdin, stdout, stderr = ssh.exec_command(res)
result_res = stdout.readlines()
stdin, stdout, stderr = ssh.exec_command(rna)
result_rna = stdout.readlines()
stdin, stdout, stderr = ssh.exec_command(dna)
result_dna = stdout.readlines()
stdin, stdout, stderr = ssh.exec_command(hic)
result_hic = stdout.readlines()
total = []
list1=[]
list2=[]
for line in result_hic:
    line=line.split('[')
    for line1 in line:
        if len(line1) > 0:
            line1=line1.split(']')
            for line2 in line1:
                if len(line2)  > 2:
                    line2=line2.split(',')
                    list1.append(line2)
for line in list1:
    line1=line[2]
    line1=int(line1)
    if line1>1024*1024*1024:
        list2.append(line)
list3=[]
list4=[]
list5=[]
for line in list2:
    line1=line[2]
    line1=int(line1)
    line2=line1/math.pow(1024,3)
    line2=round(line2)
    list3.append(line2)
    line3=line[0]
    line3=line3.split('/')
    line3=line3[2]
    list4.append(line3)
    list5.append(line[1])
for i in range(len(list3)):
    Dir.objects.create(pro=list4[i],dir=list5[i],size=list3[i])
