from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class get_obs_1(models.Model):
    dna_obs_size = models.IntegerField(default=0)
    dna_obs_spending = models.IntegerField(default=0)
    rna_obs_size = models.IntegerField(default=0)
    rna_obs_spending = models.IntegerField(default=0)
    three_genome_obs_size = models.IntegerField(default=0)
    three_genome_obs_spending = models.IntegerField(default=0)
    meta_obs_size = models.IntegerField(default=0)
    meta_obs_spending = models.IntegerField(default=0)
    res_obs_size = models.IntegerField(default=0)
    res_obs_spending = models.IntegerField(default=0)
    med_obs_size = models.IntegerField(default=0)
    med_obs_spending = models.IntegerField(default=0)
    obs_time = models.DateTimeField(default=timezone.now)
class get_obs(models.Model):
    dna_obs_size = models.IntegerField(default=0)
    dna_obs_sending = models.IntegerField(default=0)
    rna_obs_size = models.IntegerField(default=0)
    rna_obs_sending = models.IntegerField(default=0)
    three_genome_obs_size = models.IntegerField(default=0)
    three_genome_obs_spending = models.IntegerField(default=0)
    meta_obs_size = models.IntegerField(default=0)
    meta_obs_spending = models.IntegerField(default=0)
    res_obs_size = models.IntegerField(default=0)
    res_obs_spending = models.IntegerField(default=0)
    med_obs_size = models.IntegerField(default=0)
    med_obs_spending = models.IntegerField(default=0)
    obs_time = models.DateTimeField(default=timezone.now)

class get_sfs(models.Model):
    dna_sfs_size = models.IntegerField(default=0)
    dna_sfs_sending = models.IntegerField(default=0)
    rna_sfs_size = models.IntegerField(default=0)
    rna_sfs_sending = models.IntegerField(default=0)
    three_genome_sfs_size = models.IntegerField(default=0)
    three_genome_sfs_spending = models.IntegerField(default=0)
    meta_sfs_size = models.IntegerField(default=0)
    meta_sfs_spending = models.IntegerField(default=0)
    res_sfs_size = models.IntegerField(default=0)
    res_sfs_spending = models.IntegerField(default=0)
    med_sfs_size = models.IntegerField(default=0)
    med_sfs_spending = models.IntegerField(default=0)
    sfs_time = models.DateTimeField(default=timezone.now)

class get_sfs_1(models.Model):
    dna_sfs_size = models.IntegerField(default=0)
    dna_sfs_spending = models.IntegerField(default=0)
    rna_sfs_size = models.IntegerField(default=0)
    rna_sfs_spending = models.IntegerField(default=0)
    three_genome_sfs_size = models.IntegerField(default=0)
    three_genome_sfs_spending = models.IntegerField(default=0)
    meta_sfs_size = models.IntegerField(default=0)
    meta_sfs_spending = models.IntegerField(default=0)
    res_sfs_size = models.IntegerField(default=0)
    res_sfs_spending = models.IntegerField(default=0)
    med_sfs_size = models.IntegerField(default=0)
    med_sfs_spending = models.IntegerField(default=0)
    sfs_time = models.DateTimeField(default=timezone.now)


class cpu_info(models.Model):
    local_host = models.CharField(max_length=20,null=False)
    cloud_host = models.CharField(max_length=20,null=False)
    cpu_used = models.FloatField(default=0)
    cpu_time = models.DateTimeField(default=timezone.now)

class cpu_info2(models.Model):
    hostname = models.CharField(max_length=20,null=False)
    cpu_used = models.FloatField(default=0)
    cpu_time = models.DateTimeField(default=timezone.now)

class get_sfs_project(models.Model):
    sfs_project_name = models.CharField(max_length=30,null=False)
    sfs_project_path = models.CharField(max_length=100,null=False)
    sfs_project_size = models.IntegerField(default=0)
    sfs_project_spending = models.IntegerField(default=0)
    sfs_project_time = models.DateTimeField(default=timezone.now)
    

class get_obs_project_2(models.Model):
    obs_project_name = models.CharField(max_length=30,null=False)
    obs_project_path = models.CharField(max_length=100,null=False)
    obs_project_size = models.IntegerField(default=0)
    obs_project_spending = models.IntegerField(default=0)
    obs_project_time = models.DateTimeField(default=timezone.now)


class get_sfs_dir(models.Model):
    sfs_dir_name = models.CharField(max_length=20,null=False)
    sfs_dir_path = models.CharField(max_length=20,null=False)
    sfs_dir_size = models.IntegerField(default=0)
    sfs_dir_time = models.DateTimeField(default=timezone.now)


class get_obs_dir(models.Model):
    obs_dir_name = models.CharField(max_length=20,null=False)
    obs_dir_path = models.CharField(max_length=100,null=False)
    obs_dir_size = models.IntegerField(default=0)
    obs_dir_spending = models.IntegerField(default=0)
    obs_dir_time = models.DateTimeField(default=timezone.now)

class get_ecs_spending(models.Model):
    rna_ecs_spending = models.IntegerField(default=0)
    dna_ecs_spending = models.IntegerField(default=0)
    three_genome_ecs_spending = models.IntegerField(default=0)
    meta_ecs_spending = models.IntegerField(default=0)
    res_ecs_spending = models.IntegerField(default=0)
    med_ecs_spending = models.IntegerField(default=0)
    ecs_spending_time = models.DateTimeField(default=timezone.now)
#
