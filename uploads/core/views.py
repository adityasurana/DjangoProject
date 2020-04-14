
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from django.conf import settings
from subprocess import run,PIPE
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path=os.path.normpath(os.getcwd() + os.sep + os.pardir)
dir = "%s\\djangoproject\\uploads\\" % dir_path
#print(dir)

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
        return render(request, 'core/home.html', {
            'uploaded_file_url': "%s" % uploaded_file_url
        })
    return render(request, 'core/home.html')
    

def external(request):
    out=run([sys.executable, "%s\\media\\kol_rawdata_ranking.py" % dir], shell=False, stdout=PIPE)
    print(out.stdout)
    return render(request, 'core/home.html',{'data1':out.stdout}) 

def internal(request):
     out=run([sys.executable, "%s\\media\\kol_profiling_ranking.py" % dir], shell=False, stdout=PIPE)
     #print(out.stdout)
     return render(request, 'core/home.html',{'data2':out.stdout})



def twitter_tool(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        rs = OverwriteStorage().get_available_name_tweet(myfile.name) 
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/twitter_tool.html', {
            'uploaded_file_url': "%s" % uploaded_file_url
        })
    return render(request, 'core/twitter_tool.html')


def tweet_upload(request):
     out=run([sys.executable, "%s\\media\\twitter\\tweet_upload.py" % dir], shell=False, stdout=PIPE)
     print(out.stdout)
     return render(request, 'core/twitter_tool.html',{'data3':out.stdout})

def tweet(request):
    inp=request.POST.get('param')
    out=run([sys.executable, "%s\\media\\twitter\\tweet.py" % dir,inp], shell=False, stdout=PIPE)
    return render(request, 'core/twitter_tool.html',{'data4':out.stdout})




class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        try: 
            self.exists(name)
            print(name)
            path_add = "%smedia" % dir
            print(path_add)
            print(os.path.join(path_add,name))
            os.remove(os.path.join(path_add,name))
            return name
        except:
            pass

    def get_available_name_tweet(self, name):
        try:
            print(name)
            middle_path = "%smedia" % dir
            #print(middle_path, "middle")
            filepath = os.path.join(middle_path,name)  
            #print(filepath)  
            if os.path.exists(filepath):
                os.remove(filepath)
                #print("file removed")
            return name
        except:
            pass
