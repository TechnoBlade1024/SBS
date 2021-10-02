import datetime
import traceback
from multiprocessing import context

from django.http import HttpResponse, response
from django.shortcuts import render

# Create your views here.



def login(request):
    print(request.session.__dict__)
    return render(request,"index.html")
def loginuser(request):
    from .models import Users
    print('here')
    try:
        print(request.__dict__)
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        try:
            user=Users.objects.filter(username=username,password=password)
        except:
            traceback.print_exc()
            return HttpResponse("login failed")
        print(user)
        last_login=None
        if(len(user)==1):
            for user_data in user:
                last_login=user_data.last_login
                user_data.last_login=datetime.datetime.now()
                user_data.save()
            request.session.create()
            request.session['login_time']=str(datetime.datetime.now())
            print(last_login)
            context={'user':username,'prev_login':str(last_login)[:19]}
            return render(request,'home.html',context=context)
        else:
            return HttpResponse("login failed")
    except:
        traceback.print_exc()
def reguser(request):
    try:
        user=request.GET.get('username')
        password=request.GET.get('password')
        from .models import Users
        if user!=None or password !=None:
            Users.objects.create(username=user,
                         password=password,
                         last_login=datetime.datetime.now())
            return HttpResponse('User created!<br>now login using the username and password created')
        else:
            return HttpResponse('user create failed')
    except:
        traceback.print_exc()
        return HttpResponse('user create failed')

