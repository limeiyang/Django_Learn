from django.db import models

# Create your models here.
class User(models.Model):
	SEX = (
		('male', '男性'),
		('female', '女性')
	)
	nickname = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=128)
	sex = models.CharField(max_length=6, choices=SEX)
	age = models.IntegerField(default=18)
	created = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now=True)
	# 头像
	icon = models.ImageField(upload_to='icon')

	def __str__(self):
		return 'User:%s'%self.nickname


class Post(models.Model):
	title = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	author = models.ForeignKey(User, models.CASCADE)

	def __str__(self):
		return 'Post:%s->%s'%(self.title,self.author.nickname)

class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	author = models.ForeignKey(User, models.CASCADE)
	post = models.ForeignKey(Post, models.CASCADE)

	def __str__(self):
		return 'Comment:%s->%s'%(self.content,self.post.title)
