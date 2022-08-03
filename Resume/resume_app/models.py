from django.db import models

class CV_Letter_Data(models.Model):
    Name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    Job_type = models.CharField(max_length=255)
    Field_Applied = models.CharField(max_length=255)
