
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from django.conf import settings
from subprocess import run,PIPE
import os
import sys


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        rs = OverwriteStorage().get_available_name(myfile.name)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        return render(request, 'core/home.html', {
            'uploaded_file_url': "C://Users//hi//django_project/%s" % uploaded_file_url
        })
    return render(request, 'core/home.html')
    

def external(request):
    out=run([sys.executable, "C://Users//hi//django_project//uploads//media//kol_rawdata_ranking.py"], shell=False, stdout=PIPE)
    print(out.stdout)
    return render(request, 'core/home.html',{'data1':out.stdout}) 

def internal(request):
     out=run([sys.executable, "C://Users//hi//django_project//uploads//media//kol_profiling_ranking.py"], shell=False, stdout=PIPE)
     print(out.stdout)
     # print(render(request, 'core/home.html',{'data2':out.stdout}))
     return render(request, 'core/home.html',{'data2':out.stdout})



def twitter_tool(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        rs = OverwriteStorage().get_available_name_tweet(myfile.name) 
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/twitter_tool.html', {
            'uploaded_file_url': "C://Users//hi//django_project/%s" % uploaded_file_url
        })
    return render(request, 'core/twitter_tool.html')


def tweet_upload(request):
     out=run([sys.executable, "C://Users//hi//django_project//uploads//media//twitter//tweet_upload.py"], shell=False, stdout=PIPE)
     print(out.stdout)
     return render(request, 'core/twitter_tool.html',{'data3':out.stdout})

def tweet(request):
    inp=request.POST.get('param')
    out=run([sys.executable, "C://Users//hi//django_project//uploads//media//twitter//tweet.py",inp], shell=False, stdout=PIPE)
    a=out.stdout
    b=a[0:]
    c=b[0:]
    d=c[:-2]
    print(d)
    return render(request, 'core/twitter_tool.html',{'data4':d})




class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        try: 
            self.exists(name)
            print("inside class:", os.path.join('C://Users//hi//django_project//uploads//media//', name))
            os.remove(os.path.join('C://Users//hi//django_project//uploads//media//', name))
            return name
        except:
            pass

    def get_available_name_tweet(self, name):
        try:
            filePath = 'C://Users//hi//django_project//uploads//media//twitter//%s' %name      
            if os.path.exists(filePath):
                os.remove(filePath)
            # print("inside class:", os.path.join('C://Users//hi//django_project//uploads//media//twitter//', name))
            # os.remove(os.path.join('C://Users//hi//django_project//uploads//media//twitter//', name))
            return name
        except:
            pass
