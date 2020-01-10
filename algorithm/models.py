from django.db import models

# Create your models here.
'''
1.算法名称
2.算法介绍
3.算法简介

'''

# Create your models here.
class Numerical(models.Model):
    nName = models.CharField(max_length=20)
    nSynopsis = models.CharField(max_length=200)
    nIntroduce = models.TextField(max_length=2000)
    imgPath = models.CharField(max_length=20)
