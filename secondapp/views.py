import http
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from . models import Course

def show(request):
    course=Course.objects.all()
    result=''
    for c in course:
        result+=c.name+'<br>'
    return HttpResponse(result)

def insert(request):
    Course(name="데이터 분석",cnt=30)
    Course(name="데이터 수접",cnt=20)
    Course(name="웹개발",cnt=25)
    Course(name="인공지능",cnt=20)
    return HttpResponse('데이터 입력 완료')