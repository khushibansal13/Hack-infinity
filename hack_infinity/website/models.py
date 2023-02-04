from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField('user name',max_length=32)
    username=models.CharField('username',max_length=32,default=None)
    


    def create(name):
        book = Name(name=name)
        # do something with the book
        return book

    def __str__(self):
        return self.name

class user_info(models.Model):
    username=models.CharField('username',max_length=32)
    invitee=models.CharField('invitee',max_length=32)
    response=models.CharField('response',max_length=32)
    
    def create(name):
        book = Name(name=name)
        # do something with the book
        return book

    def __str__(self):
        return self.name
        
class invitation(models.Model):
    invitation=models.TextField('invitation',max_length=32)
