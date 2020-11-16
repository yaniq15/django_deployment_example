from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('KIMBO FAMILY SOON !!!')

def index(request):
    my_dict = {'insert_me':'Here my lovely wife Christelle from Toronto!'}
    return render(request, 'kimbo_app/index.html', context=my_dict)

