from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=200)
    nama_lengkap=models.CharField(max_length=200)
    jabatan=models.CharField(max_length=200)
    sosmed=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    profile=models.CharField(max_length=200)

    def __str__(self):
        return self.nama_lengkap

class Post(models.Model):
    title=models.CharField(max_length=200)
    date= models.DateTimeField(default=datetime.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    konten=models.CharField(max_length=3000)
    gambar=models.CharField(max_length=200)
    kategori=models.CharField(max_length=200,default="Dessert")

    def __str__(self):
        return self.title

class Komen(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    date= models.DateTimeField(default=datetime.now)
    komen=models.CharField(max_length=200)
   

    def __str__(self):
        return str(self.post_id)
