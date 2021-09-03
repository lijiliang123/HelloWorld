from django.http import HttpResponse
import random
from django.shortcuts import render
import datetime

content = '''
Hello!Hello World!
'''


def test(request):
    # return HttpResponse(content + ' 你是来访的第' + getRdm() + '个人！')
    value = {'Hello': content + ' 你是来访的第' + getRdm() + '个人！'}
    return render(request, 'newshow.html', context=value)   # context是关键字
    # render函数的参数说明：request固定，第二个是模板名称，第三个是上下文，其值为dic类型, key
    # 字典的key，应与模板中的变量名称相同，前端web页面才会用字典的value替代变量


def getRdm():
    a = 0
    a = random.randint(1, 100)
    return str(a)


def date(request):
    today = datetime.datetime.now()
    return render(request, 'date.html', {'now': today})
