from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 导入数据库数据
from joke.models import Article, Person

class Person_01:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.first_name = "武汉工程大学"
        self.family_name = "计算机科学"
        pass
    def full_name(self):
        return "%s - %a"%(self.first_name, self.family_name)
        pass
    pass


def index(request):
	return HttpResponse("Hello .please always face the world with a smile.")

# 定义接口
def home(request):
    title = '你好武汉工程大学'
    nav = ['动漫', '音乐', 'NBA', '足球', '直播', '时尚']
    # new一个实例对象
    person = Person_01('Bob', '男', 22)

    filter_01 = 'i am a filter_01'
    # 以字典的形式传过去
    context = {
        'title': title,
        'data': '2019-3-12',
        'text': '从沪深港通南北资金流向看，截至发稿，南向资金净流入6.69亿元，其中沪港通净流入3.6亿元，当日资金余额为416.4亿元，深港通净流入3.09亿元，当日资金余额为416.91亿元。',
        'nav': nav,
        'person': person,
        'filter_01':filter_01,
    }
    return render(request, 'article.html', context)

# 定义接口（读取数据库）
def homesql(request):
    # 读取数据库文件
    # myid = 1
    # name = Person.objects.get(id = myid)
    # sex = Person.objects.get(id = myid)
    # age = Person.objects.get(id = myid)
    person = Person.objects.get(id = 1)

    # 以字典的形式传过去
    context = {
        'person': person
    }
    return render(request, 'homesql.html',context)

