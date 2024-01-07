
from django.db import models
from django.utils import timezone
import datetime
import os



def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class pr(models.Model):
    title = models.CharField(max_length=100, default='Unknown')
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    description = models.TextField(default='the movie is too good to experience')
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.title
class adminlg(models.Model):
    username= models.CharField(max_length=100, default='Unknown')
    password= models.CharField(max_length=100, default='Unknown')
    def __str__(self):
        return self.username
    
