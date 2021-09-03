from django.http import HttpResponse
import random
from django.shortcuts import render

content = '''
Hello!Hello World!
'''


def test(request):
    # return HttpResponse(content + ' 你是来访的第' + getRdm() + '个人！')
    context = {'Hello': content + ' 你是来访的第' + getRdm() + '个人！'}
    return render(request, 'newshow.html', context)


def getRdm():
    a = 0
    a = random.randint(1, 100)
    return str(a)
