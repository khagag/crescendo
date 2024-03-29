from django.shortcuts import render
import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile,TemporaryUploadedFile
from django.core.files.storage import default_storage
settings.DATA_UPLOAD_MAX_NUMBER_FIELDS = 25000

# Create your views here.
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from django.http import HttpResponse
config = {
        "database" :{
            "host":"127.0.0.1",
            "port":3306,
        "user": "proj_user",
        "passwd": "kemo",
        "db": "crescendo"
        }
    }


djv=Dejavu(config)

from dejavu.recognize import FileRecognizer
@api_view(["GET","POST"])
def index(request):
#    song = djv.recognize(FileRecognizer,)
    if request.method == 'GET':
        print("get request")
    elif request.method == 'POST':
        print("post request")
    if request.method == 'POST':
        type(request.FILES['song'])
        #print(os.getcwd()+'file'+request.FILES['song'])
#toDo remove the file after checking
        path = default_storage.save(os.getcwd()+'/api/file/',request.FILES['song'])
        print(path)
        song=djv.recognize(FileRecognizer,path)

        return Response(song)
    return HttpResponse(request.method) 


