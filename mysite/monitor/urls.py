from django.urls import path
from . import views

app_name = 'moni'  # 这句是必须的，和之后所有的URL语句有关
urlpatterns = [
    # path(r'jiankong/',views.jiankong, name='jiankong'),
    # path(r'get_cpu/',views.get_cpu,name='get_cpu'),
    # path(r'get_cpu_time/',views.get_cpu_time,name='get_cpu_time'),
    path(r'get_project_spending/',views.get_project_spending, name='get_project_spending'),
    path(r'project_spending/',views.project_spending, name='project_spending'),
    path(r'get_project/',views.get_project, name='get_project'),
    path(r'project/',views.project, name='project'),
    path(r'sfs_sunburst/',views.sfs_sunburst, name='sfs_sunburst'),
    path(r'obs_sunburst/',views.obs_sunburst, name='obs_sunburst'),
    path(r'sfs_size/',views.sfs_size,name='sfs_size'),
    path(r'obs_size/',views.obs_size,name='obs_size'),
    path(r'sfs_spending/',views.sfs_spending,name='sfs_spending'),
    path(r'obs_spending/',views.obs_spending,name='obs_spending'),
    path(r'huawei_spending/',views.huawei_spending,name='huawei_spending'),
    path(r'huawei_spending_structure/',views.huawei_spending_structure,name='huawei_spending_structure'),
    path(r'total/',views.total,name='total'),
    path(r'get_total/',views.get_total,name='get_total'),
]
