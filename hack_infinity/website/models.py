from django.db import models

# Create your models here.
class Invitation(models.Model):
    username=models.CharField('Username',max_length=32)
    Invitee=models.CharField('Invitee',max_length=32)
    


    def create(username,invitee):
        book = Invitation(username=username,Invitee=invitee)
        # do something with the book
        return book

    def __str__(self):
        return self.username
        
class CreateEventInfo(models.Model):
    event_name=models.CharField('event_name',max_length=32)
    venue=models.CharField('venue',max_length=32)
    date=models.DateField('date',max_length=32)
    sub_event=models.CharField('sub_event',max_length=32)
    time=models.TimeField('time',max_length=32)
    


    def create(event_name,venue,date,sub_event,time):
        book = CreateEventInfo(event_name=event_name,venue=venue,date=date,sub_event=sub_event,time=time)
        # do something with the book
        return book

    def __str__(self):
        return self.event_name

class Invitation_confirmation(models.Model):
    username=models.CharField('Username',max_length=32)
    Invitee=models.CharField('Invitee',max_length=32)
    Response=models.CharField('Response',max_length=32,default='No')
    


    def create(username,invitee,response):
        book = Invitation(username=username,Invitee=invitee,Response=response)
        # do something with the book
        return book

    def __str__(self):
        return self.username

# class user_info(models.Model):
#     username=models.CharField('username',max_length=32)
#     invitee=models.CharField('invitee',max_length=32)
#     response=models.CharField('response',max_length=32)
    
#     def create(name):
#         book = Name(name=name)
#         # do something with the book
#         return book

#     def __str__(self):
#         return self.name


