import os
import re
import json
import math
import datetime
from os.path import join, getsize
import MySQLdb
# rootdir = '/local_data1/META/project'
def mysql_opera(sql):
    connection = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='devops', charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
def get_size(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        try:
            size += sum([getsize(join(root, name)) for name in files])
        except Exception as e:
            pass
        continue
    return size
def get_sfs_size(rootdir):
    list = os.listdir(rootdir)
    list1 = []
    list2 = []   #项目路径
    list4 = []   #每个项目
    list3 = []   #每个项目大小
    list5 = []   #项目编号
    list6 = []   #项目费用
    for line in list:
        if line.startswith('p'):
            line1 = os.path.join(rootdir, line)
            list1.append(line1)
    for line in list1:
        line1 = os.listdir(line)
        for line2 in line1:
            line3 = os.path.join(line, line2)
            list2.append(line3)
    for line in list2:
        line1 = get_size(line)
        list4.append(line1)
    for line in list4:
        line1=line/math.pow(1024,3)
        line1=round(line1)
        line1=int(line1)
        list3.append(line1)
    for line in list2:
        line1=line.split('/')
        line2=line1[5]
        line3=re.sub('\d{8}\D{1}', 'whfs-xs-', line2)
        line3=line3.split('.')
        line4=line3[0]
        line5=re.sub(r'\D{1}\d{2}$', '', line4)
        line6=re.split('_',line5)
        line7=line6[0]
        list5.append(line7)
    now = datetime.now()
    sfs_project_name=list5
    sfs_project_path=list2
    sfs_project_size=list3
    sfs_project_time=datetime.strftime(now,('%Y-%m-%d'))
    sql_sfs = "insert into monitor_get_sfs_project(sfs_project_name,sfs_project_path,sfs_project_size,sfs_project_time)values('%s','%s',%s,'%s')"%(sfs_project_name,sfs_project_path,sfs_project_size,sfs_project_time)
    mysql_opera(sql_sfs)
if __name__ == "__main__":
    get_sfs_size('/local_data1/META/project')

