import cloudinary
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = "posts"

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True,default='Anonymous'
    )

    body = models.CharField(
        'Body',blank=True, null=True, max_length=300, db_index=True
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )

    image = CloudinaryField('Image',blank=True,null=True)

    like_count = models.IntegerField(default=0,null=True,blank=True)


class Edit(models.Model):
    class Meta(object):
        db_table = "outer"
    
    name = models.CharField(blank=True,max_length=15)

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
