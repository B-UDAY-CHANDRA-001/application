from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class JsonData(models.Model):
    userId = models.IntegerField(10)
    id = models.IntegerField(10,primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

def validate_document(document):
    if document.size > 4*1024*1024:
        raise ValidationError("Supporting document must be <= 4MB")

class Upload(models.Model):
    UserName = models.CharField(max_length=100)
    Email = models.EmailField()
    # file = models.FileField(upload_to='uploads/', default='', validators=[FileExtensionValidator(allowed_extensions=['json'])])
    my_file = models.FileField(upload_to='doc', blank=False, validators=[validate_document, FileExtensionValidator(allowed_extensions=['json'])])

    class Meta:
        db_table = "upload"
