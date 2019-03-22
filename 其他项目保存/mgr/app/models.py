from django.db import models

# Create your models here.
class User(models.Model):
	SEX = (
		('male','男性'),
		('female','女性')
	)
	nikename = models.CharField(max_length=20)
	username = models.CharField(max_length=20,blank=True)
	password = models.CharField(max_length=20)
	age = models.IntegerField(default=18,blank=True)
	sex = models.CharField(max_length=6, choices=SEX,blank=True)
	tel = models.CharField(max_length=20,blank=True)
	others = models.CharField(max_length=100,blank=True)
	pic = models.ImageField("图片",upload_to="pic",blank=True)