'''
Created on 28-May-2022

@author: SKITWORLD
'''
from rest_framework import serializers
from .models import TrainFile, PredictFile,Predict,File
class TrainFileSerializer(serializers.ModelSerializer):
    class Meta():
        model = TrainFile
        fields = ('file',)
    
class PredictFileSerializer(serializers.ModelSerializer):
    class Meta():
        model = PredictFile
        fields = ('file',)

class PredictSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Predict
        fields = ('mail',)
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"