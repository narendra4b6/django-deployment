from django.shortcuts import render
from basic_app import views
import datetime
from datetime import time

# Create your views here.
def index(request):
    context_dict={'text':'hello world','number':100,'mydate':datetime.date.today(),'mytime':time()}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')
