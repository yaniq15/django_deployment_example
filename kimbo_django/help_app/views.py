from django.shortcuts import render
from django.http import HttpResponse
from help_app.models import Topic, AccessRecord, Webpage
# Create your views here.

# def index(request):
#     return HttpResponse('HERE MY HELP APP !!!')

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict= {'access_records':webpages_list}
    # my_dict = {'insert_me':'Here page we can find all info for help!'}
    # return render(request, 'help_app/index.html', context=my_dict)
    return render(request, 'help_app/index.html', context=date_dict)

