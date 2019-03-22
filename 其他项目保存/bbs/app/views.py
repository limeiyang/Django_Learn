from django.shortcuts import render, redirect
from django.db import IntegrityError

from django.conf import settings
from app.models import Post, User, Comment



def home(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        password = request.POST['password']
        password2 = request.POST['password2']
        sex = request.POST['sex']
        age = int(request.POST['age'])
        # 图片上传
        pic = request.FILES['icon']

        if password != password2:
            return render(request, 'register.html',
                          {'error': '两次密码不一致，请重新输入！'})
        # 创建文件
        save_path = '%s\icom'%settings.MEDIA_ROOT
        
        with open(save_path,'wb') as f:
            # 3.获取上传文件的内容,并写到创建的文件中
            for content in pic.chunks():
                f.write(content)
        try:
            user = User.objects.create(
                nickname=nickname,
                password=password,
                sex=sex,
                age=age
            )
        except IntegrityError:
            return render(request, 'register.html',
                          {'error': '用户名已存在，请重新输入！'})

        # 4.在数据库中保存上传记录
        User.objects.create(icon='icon\/%s'%pic.name)
        return redirect('/user/login/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        password = request.POST['password']

        try:
            user = User.objects.get(nickname=nickname)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': '用户不存在！'})

        # 验证密码
        if user.password == password:
            # 使用 session 机制记录登录状态
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            return redirect('/user/info/')
        else:
            return render(request, 'login.html', {'error': '密码错误！'})
    else:
        return render(request, 'login.html')


def logout(request):
    # 删除当前用户的session
    del request.session['uid']
    return render(request, 'post_list.html')


def user_info(request):
    if 'uid' in request.GET:
        uid = request.GET['uid']
        pass
    else:
        uid = request.session['uid']
        pass
    user = User.objects.get(id=uid)
    return render(request, 'user_info.html', {'user': user})

# 创建帖子
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # 获取当前用户
        uid = request.session['uid']
        user = User.objects.get(id=uid)

        # 创建帖子
        post = Post.objects.create(
            title=title,
            content=content,
            author=user
        )
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        return render(request, 'post_create.html')

# 点击帖子阅读详情
def read_post(request):
    post_id = int(request.GET['post_id'])
    post = Post.objects.get(id=post_id)

    # 获取当前帖子的所有评论
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_read.html',
                  {'post': post, 'comments': comments})


def comment(request):
    post_id = int(request.POST['post_id'])
    content = request.POST['content']

    uid = request.session['uid']
    user = User.objects.get(id=uid)
    post = Post.objects.get(id=post_id)

    Comment.objects.create(
        content=content,
        author=user,
        post=post
    )

    return redirect('/post/read/?post_id=%s' % post.id)

# 删除帖子
def post_delete(request):
    post_id = request.GET['post_id']
    obj = Post.objects.get(id=post_id)
    obj.delete()
    return redirect('/post/list/')

# 修改帖子
def post_edit(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.filter(id=post_id).update(title=title, content=content)
        # obj = Post.objects.get(id=post_id)
        # obj.update(title=title, content=content)
        return redirect('/post/read/?post_id=%s' % post_id)
        pass
    else:
        post_id = request.GET['post_id']
        post = Post.objects.get(id=post_id)
        return render(request, 'post_edit.html',{'post':post})