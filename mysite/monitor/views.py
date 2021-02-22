from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from monitor.models import *
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
import json
from django.contrib.auth.decorators import login_required
import datetime
from collections import defaultdict
@login_required
def total(request):
    return render(request,'monitor/total.html')
@login_required
def get_total(request):
    sfs_list = []
    obs_list = []
    for data_info in get_sfs_1.objects.all():
        sfs_list.append({
            'dna_sfs':data_info.dna_sfs_spending,
            'rna_sfs':data_info.rna_sfs_spending,
            'three_genome_sfs':data_info.three_genome_sfs_spending,
            'meta_sfs':data_info.meta_sfs_spending,
            'res_sfs':data_info.res_sfs_spending,
            'med_sfs':data_info.med_sfs_spending,
            'sfs_time':data_info.sfs_time,
        })
    for data_info in get_obs_1.objects.all():
        obs_list.append({
            'dna_obs':data_info.dna_obs_spending,
            'rna_obs':data_info.rna_obs_spending,
            'three_genome_obs':data_info.three_genome_obs_spending,
            'meta_obs':data_info.meta_obs_spending,
            'res_obs':data_info.res_obs_spending,
            'med_obs':data_info.med_obs_spending,
            'obs_time':data_info.obs_time,
        })
    data_dic = {}
    data_total = []
    dna_sfs_list = []
    rna_sfs_list = []
    three_genome_sfs_list = []
    meta_sfs_list = []
    res_sfs_list = []
    med_sfs_list = []
    dna_obs_list = []
    rna_obs_list = []
    meta_obs_list = []
    three_genome_obs_list = []
    res_obs_list = []
    med_obs_list = []
    for line in sfs_list:
        if line['sfs_time'].strftime('%Y-%m-%d') < '2021-02-01':
            dna_sfs_list.append(line['dna_sfs'])
            rna_sfs_list.append(line['rna_sfs'])
            three_genome_sfs_list.append(line['three_genome_sfs'])
            meta_sfs_list.append(line['meta_sfs'])
            res_sfs_list.append(line['res_sfs'])
            med_sfs_list.append(line['med_sfs'])
    for line in obs_list:
        if line['obs_time'].strftime('%Y-%m-%d') < '2021-02-01':
            dna_obs_list.append(line['dna_obs'])
            rna_obs_list.append(line['rna_obs'])
            three_genome_obs_list.append(line['three_genome_obs'])
            meta_obs_list.append(line['meta_obs'])
            res_obs_list.append(line['res_obs'])
            med_obs_list.append(line['med_obs'])
    dna_sfs_total = sum(dna_sfs_list)
    rna_sfs_total = sum(rna_sfs_list)
    three_genome_sfs_total = sum(three_genome_sfs_list)
    meta_sfs_total = sum(meta_sfs_list)
    res_sfs_total = sum(res_sfs_list)
    med_sfs_total = sum(med_sfs_list)
    dna_obs_total = sum(dna_obs_list)
    rna_obs_total = sum(rna_obs_list)
    three_genome_obs_total = sum(three_genome_obs_list)
    meta_obs_total = sum(meta_obs_list)
    res_obs_total = sum(res_obs_list)
    med_obs_total = sum(med_obs_list)
    department = ['基因组','转录组','三维','微生物','重测序','医学']
    sfs_total = [dna_sfs_total, rna_sfs_total, three_genome_sfs_total, meta_sfs_total, res_sfs_total,med_sfs_total]
    obs_total = [dna_obs_total, rna_obs_total, three_genome_obs_total, meta_obs_total, res_obs_total,med_obs_total]
    ecs_total = [42044, 6018, 17095, 2006, 4012, 4012]
    date = '2021-01'
    def list_add(a, b):
        c = []
        for i in range(len(a)):
            c.append(a[i] + b[i])
        return c
    total = list_add(list_add(sfs_total,obs_total),ecs_total)
    for i in range(len(total)):
        data_total.append({
            'sfs':sfs_total[i],
            'obs':obs_total[i],
            'department':department[i],
            'ecs':ecs_total[i],
            'total':total[i],
            'date':date,
        })
    data_dic['data'] = data_total
    return HttpResponse(json.dumps(data_dic))
@login_required
def project(request):
    return render(request,'monitor/project.html')
@login_required
def get_project(request):
    data_list = []
    data_list2 = []
    for data_info in get_sfs_project.objects.all():
        data_list.append({
            'project':data_info.sfs_project_name,
            'path':data_info.sfs_project_path,
            'size':data_info.sfs_project_size,
            'spending':data_info.sfs_project_spending,
            'datetime':data_info.sfs_project_time,
        })
    for line in data_list:
        if  line['size'] > 500 and line['project'] != 'unkown':
            datetime = line['datetime']
            datetime = datetime.strftime('%Y-%m-%d')
            size = line['size']
            path = line['path']
            project = line['project']
            data_list2.append({'project':project,'path':path,'size':size,'datetime':datetime})
    data_dic = {}
    data_dic['data'] = data_list2
    return HttpResponse(json.dumps(data_dic))
def project_spending(request):
    return render(request,'monitor/project_spending.html')
def get_project_spending(request):
    data_list = []
    data_list2 = []
    for data_info in get_sfs_project.objects.all():
        data_list.append({
            'project':data_info.sfs_project_name,
            'path':data_info.sfs_project_path,
            'size':data_info.sfs_project_size,
            'spending':data_info.sfs_project_spending,
            'datetime':data_info.sfs_project_time,
        })
    project_list = []
    spending_list = []
    for line in data_list:
        if line['size'] > 200 and line['project'] != 'unkown':
            project_list.append(line['project'])
            spending_list.append(line['spending'])
    def list_duplicates(seq):   ##统计列表重复元素的位置信息
        tally = defaultdict(list)
        for i, item in enumerate(seq):
            tally[item].append(i)
        return ((key, locs) for key, locs in tally.items()
                if len(locs) >= 1)
    project_list_sorted = []
    for line in list_duplicates(project_list):
        project_list_sorted.append(line)
    for line in project_list_sorted:
        index = line[1]
        project = line[0]
        value_list = []
        for line1 in index:
            value_list.append(spending_list[line1])
            value_list_sum = sum(value_list)
        data_list2.append({'project':project,'spending':value_list_sum})
    data_dict = {}
    data_dict['data'] = data_list2
    return HttpResponse(json.dumps(data_dict))
# @login_required
# def jiankong(request):
#     Datetime = []
#     cpu = 100
#     for i in cpu_info2.objects.all():
#         Datetime.append(datetime.strftime(i.cpu_time, "%Y-%m-%d %H:%M"))
#     content = {
#         'Datetime':Datetime,
#         'cpu':cpu,
#         }
#     return render(request,'monitor/jiankong.html',content)
# @login_required()
# def get_cpu(request):
#     cpu_list={
#         'percent':[],
#         'Datetime':[],
#     }
#     if request.is_ajax:
#         for i in cpu_info2.objects.all():
#             cpu_list['percent'].append(i.cpu_used)
#             cpu_list['Datetime'].append(datetime.strftime(i.cpu_time,"%Y-%m-%d %H:%M"))
#     return JsonResponse(cpu_list)
# @login_required
# def get_cpu_time(request):
#     cpu_list = {
#         'percent':[],
#         'Datetime':[],
#     }
#     if request.is_ajax:
#         starttime = request.GET.get('starttime').encode('utf-8')
#         endtime = request.GET.get('endtime').encode('utf-8')
#         startdate = datetime.strptime(starttime.decode().split(' ')[0], "%Y-%m-%d")
#         enddate = datetime.strptime(endtime.decode().split(' ')[0], "%Y-%m-%d")
#         for i in cpu_info.objects.filter(cpu_time__range=(startdate,enddate)):
#             cpu_list['percent'].append(i.cpu_used)
#             cpu_list['Datetime'].append(datetime.strftime(i.cpu_time,"%Y-%m-%d %H:%M"))
#             cpu_list['cpu_total']=100
#     return JsonResponse(cpu_list)
@login_required
def obs_sunburst(request):
    META_dir = list(get_obs_dir.objects.filter(obs_dir_name='meta').values_list('obs_dir_path',flat=True))
    META_size = list(get_obs_dir.objects.filter(obs_dir_name='meta').values_list('obs_dir_size',flat=True))
    RES_dir = list(get_obs_dir.objects.filter(obs_dir_name='reseq').values_list('obs_dir_path', flat=True))
    RES_size = list(get_obs_dir.objects.filter(obs_dir_name='reseq').values_list('obs_dir_size', flat=True))
    MED_dir = list(get_obs_dir.objects.filter(obs_dir_name='med').values_list('obs_dir_path', flat=True))
    MED_size = list(get_obs_dir.objects.filter(obs_dir_name='med').values_list('obs_dir_size', flat=True))
    Three_genome_dir = list(get_obs_dir.objects.filter(obs_dir_name='3dgenome').values_list('obs_dir_path', flat=True))
    Three_genome_size = list(get_obs_dir.objects.filter(obs_dir_name='3dgenome').values_list('obs_dir_size', flat=True))
    RNA_dir = list(get_obs_dir.objects.filter(obs_dir_name='rna').values_list('obs_dir_path', flat=True))
    RNA_size = list(get_obs_dir.objects.filter(obs_dir_name='rna').values_list('obs_dir_size', flat=True))
    DNA_dir = list(get_obs_dir.objects.filter(obs_dir_name='dna').values_list('obs_dir_path', flat=True))
    DNA_size = list(get_obs_dir.objects.filter(obs_dir_name='dna').values_list('obs_dir_size', flat=True))
    dict_for_html = {
        'META_dir':META_dir,
        'META_size':META_size,
        'RES_dir':RES_dir,
        'RES_size':RES_size,
        'MED_dir':MED_dir,
        'MED_size':MED_size,
        'Three_genome_dir':Three_genome_dir,
        'Three_genome_size':Three_genome_size,
        'RNA_dir':RNA_dir,
        'RNA_size':RNA_size,
        'DNA_dir':DNA_dir,
        'DNA_size':DNA_size,
    }
    return render(request,'monitor/obs_sunburst.html',dict_for_html)
@login_required
def sfs_sunburst(request):
    META_time = list(get_sfs_dir.objects.filter(sfs_dir_name='META').values_list('sfs_dir_time', flat=True))
    meta_latest_time = META_time[-1]
    META_dir = list(get_sfs_dir.objects.filter(sfs_dir_name='META',sfs_dir_time=meta_latest_time).values_list('sfs_dir_path',flat=True))
    META_size = list(get_sfs_dir.objects.filter(sfs_dir_name='META',sfs_dir_time=meta_latest_time).values_list('sfs_dir_size',flat=True))
    RES_time = list(get_sfs_dir.objects.filter(sfs_dir_name='RES').values_list('sfs_dir_time', flat=True))
    res_latest_time = RES_time[-1]
    RES_dir = list(get_sfs_dir.objects.filter(sfs_dir_name='RES',sfs_dir_time=res_latest_time).values_list('sfs_dir_path', flat=True))
    RES_size = list(get_sfs_dir.objects.filter(sfs_dir_name='RES',sfs_dir_time=res_latest_time).values_list('sfs_dir_size', flat=True))
    MED_time = list(get_sfs_dir.objects.filter(sfs_dir_name='MED').values_list('sfs_dir_time', flat=True))
    med_latest_time = MED_time[-1]
    MED_dir = list(get_sfs_dir.objects.filter(sfs_dir_name='MED',sfs_dir_time=med_latest_time).values_list('sfs_dir_path', flat=True))
    MED_size = list(get_sfs_dir.objects.filter(sfs_dir_name='MED',sfs_dir_time=med_latest_time).values_list('sfs_dir_size', flat=True))
    Three_genome_time = list(get_sfs_dir.objects.filter(sfs_dir_name='3D').values_list('sfs_dir_time', flat=True))
    three_genome_latest = Three_genome_time[-1]
    Three_genome_dir = list(get_sfs_dir.objects.filter(sfs_dir_name='3D',sfs_dir_time=three_genome_latest).values_list('sfs_dir_path', flat=True))
    Three_genome_size = list(get_sfs_dir.objects.filter(sfs_dir_name='3D',sfs_dir_time=three_genome_latest).values_list('sfs_dir_size', flat=True))
    RNA_time = list(get_sfs_dir.objects.filter(sfs_dir_name='RNA').values_list('sfs_dir_time', flat=True))
    rna_latest_time = RNA_time[-1]
    RNA_dir = list(get_sfs_dir.objects.filter(sfs_dir_name='RNA',sfs_dir_time=rna_latest_time).values_list('sfs_dir_path', flat=True))
    RNA_size = list(get_sfs_dir.objects.filter(sfs_dir_name='RNA',sfs_dir_time=rna_latest_time).values_list('sfs_dir_size', flat=True))
    DNA_time = list(get_sfs_dir.objects.filter(sfs_dir_name='DNA').values_list('sfs_dir_time', flat=True))
    dna_latest_time = DNA_time[-1]
    DNA_dir = list(get_sfs_dir.objects.filter(sfs_dir_name='DNA',sfs_dir_time=dna_latest_time).values_list('sfs_dir_path', flat=True))
    DNA_size = list(get_sfs_dir.objects.filter(sfs_dir_name='DNA',sfs_dir_time=dna_latest_time).values_list('sfs_dir_size', flat=True))
    META = dict(zip(META_dir,META_size))
    META_list = sorted(META.items(),key = lambda kv:(kv[1], kv[0]))
    META_list = META_list[-3:]
    META_DIR = []
    META_SIZE = []
    for line in META_list:
        line = list(line)
        META_DIR.append(line[0])
        META_SIZE.append(line[1])
    RES = dict(zip(RES_dir, RES_size))
    RES_list = sorted(RES.items(), key=lambda kv: (kv[1], kv[0]))
    RES_list = RES_list[-3:]
    RES_DIR = []
    RES_SIZE = []
    for line in RES_list:
        line = list(line)
        RES_DIR.append(line[0])
        RES_SIZE.append(line[1])
    MED = dict(zip(MED_dir, MED_size))
    MED_list = sorted(MED.items(), key=lambda kv: (kv[1], kv[0]))
    MED_list = MED_list[-3:]
    MED_DIR = []
    MED_SIZE = []
    for line in MED_list:
        line = list(line)
        MED_DIR.append(line[0])
        MED_SIZE.append(line[1])
    Three_genome = dict(zip(Three_genome_dir, Three_genome_size))
    Three_genome_list = sorted(Three_genome.items(), key=lambda kv: (kv[1], kv[0]))
    Three_genome_list = Three_genome_list[-3:]
    Three_genome_DIR = []
    Three_genome_SIZE = []
    for line in Three_genome_list:
        line = list(line)
        Three_genome_DIR.append(line[0])
        Three_genome_SIZE.append(line[1])
    RNA = dict(zip(RNA_dir, RNA_size))
    RNA_list = sorted(RNA.items(), key=lambda kv: (kv[1], kv[0]))
    RNA_list = RNA_list[-3:]
    RNA_DIR = []
    RNA_SIZE = []
    for line in RNA_list:
        line = list(line)
        RNA_DIR.append(line[0])
        RNA_SIZE.append(line[1])
    DNA = dict(zip(DNA_dir, DNA_size))
    DNA_list = sorted(DNA.items(), key=lambda kv: (kv[1], kv[0]))
    DNA_list = DNA_list[-3:]
    DNA_DIR = []
    DNA_SIZE = []
    for line in DNA_list:
        line = list(line)
        DNA_DIR.append(line[0])
        DNA_SIZE.append(line[1])
    dict_for_html = {
        'META_DIR':META_DIR,
        'META_SIZE':META_SIZE,
        'RES_DIR':RES_DIR,
        'RES_SIZE':RES_SIZE,
        'MED_DIR':MED_DIR,
        'MED_SIZE':MED_SIZE,
        'Three_genome_DIR':Three_genome_DIR,
        'Three_genome_SIZE':Three_genome_SIZE,
        'RNA_DIR':RNA_DIR,
        'RNA_SIZE':RNA_SIZE,
        'DNA_DIR': DNA_DIR,
        'DNA_SIZE': DNA_SIZE,
        
    }
    return render(request,'monitor/sfs_sunburst.html',dict_for_html)
@login_required
def sfs_size(request):
    dna_sfs_size = list(get_sfs_1.objects.values_list('dna_sfs_size',flat=True))
    rna_sfs_size = list(get_sfs_1.objects.values_list('rna_sfs_size',flat=True))
    three_genome_sfs_size = list(get_sfs_1.objects.values_list('three_genome_sfs_size',flat=True))
    meta_sfs_size = list(get_sfs_1.objects.values_list('meta_sfs_size',flat=True))
    res_sfs_size = list(get_sfs_1.objects.values_list('res_sfs_size',flat=True))
    med_sfs_size = list(get_sfs_1.objects.values_list('med_sfs_size',flat=True))
    sfs_time = list(get_sfs_1.objects.values_list('sfs_time',flat=True))
    dna_sfs_size1 = dna_sfs_size[-7:]
    rna_sfs_size1 = rna_sfs_size[-7:]
    three_genome_sfs_size1 = three_genome_sfs_size[-7:]
    meta_sfs_size1 = meta_sfs_size[-7:]
    res_sfs_size1 = res_sfs_size[-7:]
    med_sfs_size1 = med_sfs_size[-7:]
    sfs_time1 = sfs_time[-7:]
    sfs_time2 = []
    for line in sfs_time1:
        line = line.strftime('%Y-%m-%d')
        sfs_time2.append(line)
    dict_for_html = {
         "dna":dna_sfs_size1,
         "rna":rna_sfs_size1,
         "3d":three_genome_sfs_size1,
         "meta":meta_sfs_size1,
         "res":res_sfs_size1,
         "med":med_sfs_size1,
         "time":sfs_time2,
        }
    return render(request,'monitor/sfs_size.html',dict_for_html)
@login_required
def sfs_spending(request):
    dna_sfs_spending = list(get_sfs_1.objects.values_list('dna_sfs_spending',flat=True))
    rna_sfs_spending = list(get_sfs_1.objects.values_list('rna_sfs_spending',flat=True))
    three_genome_sfs_spending = list(get_sfs_1.objects.values_list('three_genome_sfs_spending',flat=True))
    meta_sfs_spending = list(get_sfs_1.objects.values_list('meta_sfs_spending',flat=True))
    res_sfs_spending = list(get_sfs_1.objects.values_list('res_sfs_spending',flat=True))
    med_sfs_spending = list(get_sfs_1.objects.values_list('med_sfs_spending',flat=True))
    sfs_time = list(get_sfs_1.objects.values_list('sfs_time', flat=True))
    dna_sfs_spending1 = dna_sfs_spending[-7:]
    rna_sfs_spending1 = rna_sfs_spending[-7:]
    three_genome_sfs_spending1 = three_genome_sfs_spending[-7:]
    meta_sfs_spending1 = meta_sfs_spending[-7:]
    res_sfs_spending1 = res_sfs_spending[-7:]
    med_sfs_spending1 = med_sfs_spending[-7:]
    sfs_time1 = sfs_time[-7:]
    sfs_time2 = []
    for line in sfs_time1:
        line = line.strftime('%Y-%m-%d')
        sfs_time2.append(line)
    dict_for_html = {
         "dna":dna_sfs_spending1,
         "rna":rna_sfs_spending1,
         "3d":three_genome_sfs_spending1,
         "meta":meta_sfs_spending1,
         "res":res_sfs_spending1,
         "med":med_sfs_spending1,
         "time": sfs_time2,
        }
    return render(request,'monitor/sfs_spending.html',dict_for_html)
@login_required
def obs_size(request):
    dna_obs_size = list(get_obs_1.objects.values_list('dna_obs_size',flat=True))
    rna_obs_size = list(get_obs_1.objects.values_list('rna_obs_size',flat=True))
    three_genome_obs_size = list(get_obs_1.objects.values_list('three_genome_obs_size',flat=True))
    meta_obs_size = list(get_obs_1.objects.values_list('meta_obs_size',flat=True))
    res_obs_size = list(get_obs_1.objects.values_list('res_obs_size',flat=True))
    med_obs_size = list(get_obs_1.objects.values_list('med_obs_size',flat=True))
    obs_time = list(get_obs_1.objects.values_list('obs_time', flat=True))
    dna_obs_size1 = dna_obs_size[-7:]
    rna_obs_size1 = rna_obs_size[-7:]
    three_genome_obs_size1 = three_genome_obs_size[-7:]
    meta_obs_size1 = meta_obs_size[-7:]
    res_obs_size1 = res_obs_size[-7:]
    med_obs_size1 = med_obs_size[-7:]
    obs_time1 = obs_time[-7:]
    obs_time2 = []
    for line in obs_time1:
        line = line.strftime('%Y-%m-%d')
        obs_time2.append(line)
    dict_for_html = {
         "dna":dna_obs_size1,
         "rna":rna_obs_size1,
         "3d":three_genome_obs_size1,
         "meta":meta_obs_size1,
         "res":res_obs_size1,
         "med":med_obs_size1,
         "time": obs_time2,
        }
    return render(request,'monitor/obs_size.html',dict_for_html)
@login_required
def obs_spending(request):
    dna_obs_spending = list(get_obs_1.objects.values_list('dna_obs_spending',flat=True))
    rna_obs_spending = list(get_obs_1.objects.values_list('rna_obs_spending',flat=True))
    three_genome_obs_spending = list(get_obs_1.objects.values_list('three_genome_obs_spending',flat=True))
    meta_obs_spending = list(get_obs_1.objects.values_list('meta_obs_spending',flat=True))
    res_obs_spending = list(get_obs_1.objects.values_list('res_obs_spending',flat=True))
    med_obs_spending = list(get_obs_1.objects.values_list('med_obs_spending',flat=True))
    obs_time = list(get_obs_1.objects.values_list('obs_time', flat=True))
    dna_obs_spending1 = dna_obs_spending[-7:]
    rna_obs_spending1 = rna_obs_spending[-7:]
    three_genome_obs_spending1 = three_genome_obs_spending[-7:]
    meta_obs_spending1 = meta_obs_spending[-7:]
    res_obs_spending1 = res_obs_spending[-7:]
    med_obs_spending1 = med_obs_spending[-7:]
    obs_time1 = obs_time[-7:]
    obs_time2 = []
    for line in obs_time1:
        line = line.strftime('%Y-%m-%d')
        obs_time2.append(line)
    dict_for_html = {
         "dna":dna_obs_spending1,
         "rna":rna_obs_spending1,
         "3d":three_genome_obs_spending1,
         "meta":meta_obs_spending1,
         "res":res_obs_spending1,
         "med":med_obs_spending1,
         "time": obs_time2,
        }
    return render(request,'monitor/obs_spending.html',dict_for_html)
@login_required
def huawei_spending(request):
    return render(request,'monitor/huawei_spending.html')
@login_required
def huawei_spending_structure(request):
    return render(request,'monitor/huawei_spending_structure.html')
