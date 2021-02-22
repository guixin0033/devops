import paramiko
import os
import time
from threading import Timer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from monitor.models import Test
ip = "192.168.2.160"
port = 22
user = "guixin"
password = "123456"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, user, password, timeout=10)
cp = "cat /lustre/Work/guixin/get_cluster_data/list"
stdin, stdout, stderr = ssh.exec_command(cp)
result = stdout.readlines()
total = []
for line in result:
    line = line.split()
    total.append(line)
def clear(i,j):
    for line in i:
        line = line.strip(',')
        line = line.strip('[')
        line = line.strip(']')
        j.append(line)
count = len(total)

while count > 0:
    obs = []
    sfs = []
    local1 = []
    local = []
    datatime = []
    count1 = 0
    clear(total[4],obs)
    obs = list(map(int,obs))
    # print(obs)
    clear(total[3],sfs)
    sfs = list(map(int,sfs))
    # print(sfs)
    clear(total[2],local1)
    local1 = list(map(float,local1))
    local = list(map(int,local1))
    # print(local)
    datatime = ''.join(total[0])
    RNA = ['转录组',local[0],sfs[0],obs[0],datatime]
    DNA = ['基因组',local[1],sfs[1],obs[1],datatime]
    RES = ['重测序',local[2],sfs[2],obs[2],datatime]
    hic = ['三维组',local[3],sfs[3],obs[3],datatime]
    MED = ['医学',local[4],sfs[4],obs[4],datatime]
    META = ['微生物',local[5],sfs[5],obs[5],datatime]
    l = [RNA,DNA,RES,hic,MED,META]
    for line in l:
        Test.objects.get_or_create(pro=line[0],local=line[1],sfs=line[2],obs=line[3],datatime=line[4])
    count = count - 5
    count1 = count1 + 1
    total = total[5*count1:]







