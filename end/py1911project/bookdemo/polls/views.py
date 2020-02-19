from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import ListView
from .models import *
from django.contrib.auth import authenticate, login as lin, logout as lot
from .forms import LoginForm, RegistForm


# Create your views here.
def index(request):
    issues = Issue.objects.all()
    return render(request, 'polls_index.html', {'issues': issues})


def detail(request, issueid):
    issue = Issue.objects.get(id=issueid)
    if request.method == 'GET':
        if request.user and request.user.username != "":
            if issue in request.user.issues.all():
                print('已经投过票')
                url = reverse('polls:result', args=(issueid,))
                return redirect(to=url)
            else:
                try:
                    print(issue, '---')
                    return render(request, 'polls_detail.html', {'issue': issue})
                except Exception as e:
                    print(e, '异常结果')
                    return HttpResponse("问题不合法")
        else:
            url = reverse('polls:login') + "?next=/polls/detail/" + issueid + '/'
            return redirect(to=url)
    elif request.method == 'POST':
        choiceid = request.POST.get("num")
        try:
            option = Option.objects.get(id=choiceid)
            option.votes += 1
            option.save()
            request.user.issues.add(Issue.objects.get(id=issueid))
            url = reverse('polls:result', args=(issueid,))
            return redirect(to=url)
        except:
            return HttpResponse("选项不合法")


def pollsnum(request, issueid):
    try:
        issue = Issue.objects.get(id=issueid)
        return render(request, 'polls_votesnum.html', {'issue': issue})
    except:
        return HttpResponse("问题不合法")


class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls_index.html"
    # queryset 指明返回的结果列表
    queryset = Issue.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "issues"

    # 方法一、继承的TemplateView
    # template_name = "polls_index.html"
    # def get_context_data(self, **kwargs):
    #     return {"issue":Issue.objects.all()}


class DetailView(View):
    def get(self, request, issueid):
        issue = Issue.objects.get(id=issueid)
        return render(request, 'polls_detail.html', {'issue': issue})

    def post(self, request, issueid):
        choiceid = request.POST.get("num")
        try:
            option = Option.objects.get(id=choiceid)
            option.votes += 1
            option.save()
            url = reverse('polls:result', args=(issueid,))
            return redirect(to=url)
        except:
            return HttpResponse("选项不合法")


class ResultView(View):
    def get(self, request, issueid):
        try:
            issue = Issue.objects.get(id=issueid)
            return render(request, 'polls_votesnum.html', {'issue': issue})
        except:
            return HttpResponse("问题不合法")


def login(request):
    if request.method == "GET":
        lf = LoginForm()
        return render(request, 'login.html', {'lf': lf})
    elif request.method == "POST":
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(username=username, password=password)
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                lin(request, user)
                next = request.GET.get('next')
                print('取得next参数为：', next)
                if next:
                    url = next
                else:
                    url = reverse('polls:index')
                return redirect(to=url)
            else:
                # url = reverse('polls:login')
                # return redirect(to=url)
                return render(request, 'login.html', {'errors': '用户名或密码错误'})
        else:
            return HttpResponse("未知错误")


def logout(request):
    # 调用django的登出方法 目的是为了删除cookie
    lot(request)
    url = reverse('polls:index')
    return redirect(to=url)


def regist(request):
    if request.method == "GET":
        rf = RegistForm()
        return render(request, 'regist.html', {'rf': rf})
    elif request.method == "POST":
        rf = RegistForm(request.POST)
        if rf.is_valid():
            print(rf.cleaned_data['username'],'==')
            username = rf.cleaned_data['username']
            password = rf.cleaned_data['password']
            password2 = rf.cleaned_data['password2']
            if User.objects.filter(username=username).count() > 0:
                return render(request, 'regist.html', {'errors': '用户名已存在'})
            else:
                if password == password2:
                    # User.objects.create_user(username=username, password=password)
                    rf.save()
                    url = reverse('polls:login')
                    return redirect(to=url)
                else:
                    return render(request, 'regist.html', {'errors': '密码不一致'})
        else:
            return HttpResponse("未知错误")
