from django.db import models

# Create your models here.

# 음식점 데이터 저장
class stores(models.Model):
    store_id = models.IntegerField()
    region = models.CharField(max_length=255, null=False)
    store_name = models.CharField(max_length=255, null=False)
    store_x = models.FloatField(null=True)
    store_y = models.FloatField(null=True)
    store_addr = models.CharField(max_length=255, null=False)
    store_addr_new = models.CharField(max_length=255, null=True)
    store_tel = models.CharField(max_length=255, null=True)
    open_hours = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    s_link = models.IntegerField(null=False)
    siksin_avg_score = models.FloatField(null=True)
    dining_avg_score = models.FloatField(null=True)
    google_avg_score = models.FloatField(null=True)
    naver_avg_score = models.FloatField(null=True)
    pick_avg_score= models.FloatField(null=True)
    menu = models.CharField(max_length=255, null=True)


# 검색 기록 저장 (지역, 동, 메뉴)
class history(models.Model):
    region = models.CharField(max_length=255, null=True)
    addr = models.CharField(max_length=255, null=True)
    menu = models.CharField(max_length=255, null=True)