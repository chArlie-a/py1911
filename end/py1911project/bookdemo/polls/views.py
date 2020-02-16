from django.shortcuts import render, redirect, reverse
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
        print('post')
        print(type(request.POST.get("p")))
        if request.POST.get("p") == "1":
            issue.option1_votes += 1
        elif request.POST.get("p") == "2":
            issue.option2_votes += 1
        elif request.POST.get("p") == "3":
            issue.option3_votes += 1
        elif request.POST.get("p") == "4":
            issue.option4_votes += 1
        issue.save()
    return render(request, 'polls_votesnum.html', {'issue': issue})


def pollsnum(request,issueid):
    url = reverse('polls:index')
    return redirect(to=url)
