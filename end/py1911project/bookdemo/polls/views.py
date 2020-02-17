from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import ListView

from .models import Issue, Option


# Create your views here.
def index(request):
    issues = Issue.objects.all()
    return render(request, 'polls_index.html', {'issues': issues})


def detail(request, issueid):
    issue = Issue.objects.get(id=issueid)
    if request.method == 'GET':
        return render(request, 'polls_detail.html', {'issue': issue})
    elif request.method == 'POST':
        choiceid = request.POST.get("num")
        try:
            option = Option.objects.get(id=choiceid)
            option.votes += 1
            option.save()
            url = reverse('polls:pollsnum', args=(issueid,))
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
    def get(self,request,issueid):
        try:
            issue = Issue.objects.get(id=issueid)
            return render(request, 'polls_votesnum.html', {'issue': issue})
        except:
            return HttpResponse("问题不合法")
