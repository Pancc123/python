from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    #return HttpResponse("Hello Django")
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        #username = 'admin'
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            #return HttpResponse('login success!')
            return HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user', username, 3600)   #添加浏览器Cookie
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error !'})


def event_manage(request):

    #username = request.COOKIES.get('user', '')    #读取浏览器cookie
    username = request.session.get('user', '')
    if username:
       return render(request, 'event_manage.html', {"user": username})


