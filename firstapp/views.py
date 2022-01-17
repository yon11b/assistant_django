from xml.etree.ElementTree import QName
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum
def insert(request):
    # 1-linux
    Curriculum.objects.create(name='linux')
    
    # 2-python
    c=Curriculum(name='python')
    c.save()

    # 3-html/css/js
    Curriculum(name='python').save()

    # 4-django
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')


def show(request):
    curriculum=Curriculum.objects.all()
    result=''
    for c in curriculum:
        result+=c.name+'<br>'
    return HttpResponse(result)

def index1(request):
    return HttpResponse('<u>Hello</u>')

def index2(request):
    return HttpResponse('<u>Hi</u>')

def main(request):
    return HttpResponse('<u>Main</u>')
