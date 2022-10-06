from django.db import models

# Create your models here.
class apiModel(models.Model):
    xml_file = models.FilePathField(path ="C:/xmls")
    def __str__(self):
        return self.xml_file