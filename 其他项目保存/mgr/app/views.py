from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.core.files.base import ContentFile

from app.models import User
from django.conf import settings
from app.check_code import create_validate_code
# Create your views here.
def login(request):
	if request.method == 'POST':
		nikename = request.POST['nikename']
		password = request.POST['password']

		try:
			user = User.objects.get(nikename=nikename)
		except User.DoesNotExist:
			return render(request, 'login.html', {'error': '用户不存在！'})

        # 验证密码
		if user.password == password:
        # 使用 session 机制记录登录状态
			request.session['uid'] = user.id
			return redirect('/userDetail/')
		else:
			return render(request, 'login.html', {'error': '密码错误！'})
	else:
		return render(request, 'login.html')

def regist(request):
	if request.method == 'POST':
		code = request.POST['code']
		nikename = request.POST['nikename']
		username = request.POST['username']
		password = request.POST['password']
		age = request.POST['age']
		sex = request.POST['sex']
		tel = request.POST['tel']
		others = request.POST['others']
		print("1111111")
		print(request.session['code'])
		if request.session['code'] in code:
			print("22222222")

			User.objects.create(
				nikename = nikename,
				username = username,
				password = password,
				age = age,
				sex = sex,
				tel = tel,
				others = others
			)
			return redirect('/login/')
			pass
		else:
			print("2333333")
			return render(request, 'regist.html')
	else:
		get_code(request)
		return render(request, 'regist.html')

def userList(request):
	user = User.objects.all()
	return render(request, 'userList.html',{'users':user})

def userDetail(request):
	if request.method == 'POST':
		pic=request.FILES.get('pic')
		img =User(pic=request.FILES.get('pic'))
		# img.save()
		# img = ContentFile(request.FILES['pic'].read())
		# img.save()
		print(img)
		pic ='/pic/'+str(pic)
		print(pic)
		oid = request.session['oid']
		User.objects.filter(id=oid).update(pic=pic)
		user = User.objects.get(id=oid)
		return render(request,'userDetail.html',{'user':user})
		pass
	else:
		if 'uid' in request.GET:
			uid = request.GET['uid']
			request.session['oid']=uid
		else:
			uid = request.session['uid']
		user = User.objects.get(id=uid)
		return render(request,'userDetail.html',{'user':user})

def get_code(request):
	# 获取验证码
	'''
	def picupload(request, username):
	    if 'POST' == request.method:
	      form = PicForm(request.POST, request.FILES)
	      if form.is_valid():
	          dest = os.path.join(setting.MEDIA_ROOT, username, "default.jpg")
	          if os.path.exists(dest):
	              os.remove(dest)
	          reqfile = form.cleaned_data['pic']
	          with open(dest, "wb+") as destination:
	          for chunk in reqfile.chunks():
	              destination.write(chunk)
	          return dest
	'''
	img, strs = create_validate_code()
	namecode='codeimg'
	img.save('%s/%s.png'%(settings.MEDIA_ROOT,namecode))
	request.session['code']=strs
	print(strs)

def user_update(request):
	if request.method == 'POST':
		uid = request.POST['uid']
		nikename = request.POST['nikename']
		username = request.POST['username']
		password = request.POST['password']
		age = request.POST['age']
		sex = request.POST['sex']
		tel = request.POST['tel']
		others = request.POST['others']

		User.objects.filter(id=uid).update(
			nikename = nikename,
			username = username,
			password = password,
			age = age,
			sex = sex,
			tel = tel,
			others = others
		)
		return redirect('/user_update/?uid=%s'%uid)
		pass
	else:
		uid = request.GET['uid']
		user = User.objects.get(id=uid)
		return render(request,'userUpdate.html',{'user':user})
		pass
def user_delete(request):
	uid = request.GET['uid']
	obj = User.objects.get(id=uid)
	obj.delete()
	return redirect('/userList/')