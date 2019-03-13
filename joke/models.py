from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 16)
	sub_title = models.CharField(max_length = 16)
	date = models.DateField(auto_now_add = True)
	text = models.TextField()


class Person(models.Model):
	SEX = (
			('male', '男性'),
			('female', '女性')
		)
	name = models.CharField(max_length = 16)
	sex = models.CharField(max_length = 8, choices = SEX)
	age = models.IntegerField()