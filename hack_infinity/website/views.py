from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import Invitation,Invitation_confirmation,CreateEventInfo,events   

from django.db import connection
# Create your views here.def register(request):
# def send_mail(request):
    # return render(request,'send_mail.html')
def invite(request):
    return render(request,'invite.html')

def inviting(request):
    username=request.GET['admin']
    numb_of_people=request.GET['users']
    list=numb_of_people.split(',')
    # print(username)
    # curr=request.user
    # invitee=User.username
    invitee=username
    print(list)
    # print(numb_of_people)
    for i in list:
        print(i)
        invitation=Invitation.create(username=i,invitee=invitee)
        invitation.save()
    return render(request,'landing_page.html',{'msg':numb_of_people,'msg2':username})

def create_event(request):
    return render(request,'create_event.html')

def create_schedule(request):
    event_name=request.GET.get('event_name')
    venue=request.GET.get('venue')
    date=request.GET.get('date')

    list_event=['event1','event2','event3','event4','event5','event6'] 
    list_time=['time1','time2','time3','time4','time5','time6'] 
    x=0
    for i in range(6):
        # if x==0:
            sub_event=request.GET.get(list_event[i])
            time=request.GET.get(list_time[i])
            new=CreateEventInfo.create(event_name=event_name,venue=venue,date=date,sub_event=sub_event,time=time)
            new.save()
            # x+=1
        # else:
        #     return render(request,'landing_page.html ')
    event1=events()
    event1.event=request.GET.get('event1')
    event1.time=request.GET.get('time1')

    event2=events()
    event2.event=request.GET.get('event2')
    event2.time=request.GET.get('time2')
    
    event3=events()
    event3.event=request.GET.get('event3')
    event3.time=request.GET.get('time3')
    
    event4=events()
    event4.event=request.GET.get('event4')
    event4.time=request.GET.get('time4')
    
    event5=events()
    event5.event=request.GET.get('event5')
    event5.time=request.GET.get('time5')
    
    event6=events()
    event6.event=request.GET.get('event6')
    event6.time=request.GET.get('time6')
    
    eves=[event1,event2,event3,event4,event5,event6]
    return render(request,'schedule.html',{'event_name':event_name,'venue':venue,'date':date,'eves':eves})

def show_event_details(request):
    
    values=CreateEventInfo.objects.values_list('event_name')
    x=list(values)
    print(x)
    for i in x:
        if i==('hackathon',):
            print("\n yes")
    return render(request,'index.html')

    # invitee=request.user
    # print(invitee)
    # return render(request,'send_mail.html')
# def store_data(request):
        # name=request.GET['trynowbitch']
        # book.save()
        # t=Name()
        # print(t)
        # return render(request,'show_data.html',{'name':name})

# def display_names(request):
        # values=Name.objects.all()
        # val="NO data available"
        # list=[]
        # for i in (values):
        #         print(i)
        #         x=str(i)
        #         list.append(x)
        #         if x=="first":
        #                 print("code succesful")
        #                 val=x
        #                 break
                
        #                 # return render(request,'display_names.html',{'val':val}) 
        # print(val)
        # return render(request,'display_names.html',{'val':val}) 
                        
        # print(list)
        # print(val)

def index(request):
        return render(request,'index.html')
def registration(request):
        # pass
        return render(request,'registration.html')
        
def register(request):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        pw=request.POST['pw']
        cpw=request.POST['cpw']
        # type=request.POST['user_type']
        # msg=""
        if cpw!=pw:
            return render(request,'index.html',{'msg':"Password not matching !!!"}) 

        elif User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            msg=("Username Already Exists \n Please select different username ")
            return render(request,'index.html',{'msg':msg}) 

    
        user=User.objects.create_user(username=username,password=pw,email=email,first_name=firstname,last_name=lastname)
        user.save();

        return render(request,'login.html') 

def login(request):
    return render(request,'login.html')
    
def logging(request):
        username=request.POST['username']

        password=request.POST['pw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
                return render(request,'landing_page.html',{'user':user  })
         
# def landing_page(request):
#     return render(request,'landing_page.html')
def logout(request):

    auth.logout(request)
    return render(request,'index.html')
