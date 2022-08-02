from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FileUploadParser,FormParser,JSONParser
from .serializers import TrainFileSerializer, PredictFileSerializer, PredictSerializer,FileSerializer
from spamdetection_ml.spamdetection_ml import train,predict, predict_file
from .models import TrainFile , PredictFile,Predict
import csv
import pandas as pd
# Create your views here.

#from .models import CartItem
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.response import Response
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer

#@api_view(['POST'])
#@renderer_classes([JSONRenderer])   
#def train(self, request, filename, format=None):
#    file_obj = request.FILES['file']
    #train(file_obj)
#    return Response({"status": "success", "data": 'Success'}, status=status.HTTP_200_OK)

class PredictFileView(APIView):
   # parser_classes = [MultiPartParser,]
    parser_class = (FileUploadParser ,)
    def post(self, request, *args, **kwargs):
        file_serializer = PredictFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            predictFile = PredictFile.objects.last()
            #print(trainFile.file)
            file_path = predict_file(predictFile.file)
            
        
            FilePointer = open(file_path,"r")
            response = HttpResponse(FilePointer, content_type='text')
           
            #response['Content-Disposition'] = 'attachment; filename='+file_path

            return response
            
         
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainView(APIView):
    parser_class = (FileUploadParser ,)
    def post(self, request, *args, **kwargs):
    
        file_serializer = TrainFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            trainFile = TrainFile.objects.last()
            #print(trainFile.file)ss
            res= train(trainFile.file)
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictView(APIView):
    #parser_classes = (JSONParser, MultiPartParser,FormParser)
    def post(self, request, *args, **kwargs):
        #predict_data = JSONParser().parse(request)
      #  print(self.data)
      #  print(request.data)
        predict_serializer = PredictSerializer(data=request.data)
        if predict_serializer.is_valid():
            predict_serializer.save()
            predict_data = Predict.objects.last()
            #print(trainFile.file)
            res = predict(predict_data.mail)
            
        return Response({"status": "success", "data": res}, status=status.HTTP_200_OK)
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)
            
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
#class SpamDetactionAPI(APIView):
#    def post(self, request):
#        serializer = CartItemSerializer(data=request.data)
#        if serializer.is_valid():
 #           serializer.save()
 #           return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 #       else:
#            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST