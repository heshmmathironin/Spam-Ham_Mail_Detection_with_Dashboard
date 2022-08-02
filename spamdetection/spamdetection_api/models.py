from django.db import models

# Create your models here.
class TrainFile(models.Model):
    file = models.FileField(blank=False, null=False)
    status = models.CharField(max_length=20, default='new')
    timestamp = models.DateTimeField(auto_now_add=True)
class PredictFile(models.Model):
    file = models.FileField(blank=False, null=False)
    status = models.CharField(max_length=20, default='new')
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Predict(models.Model):
    mail = models.CharField(max_length=1000, blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name