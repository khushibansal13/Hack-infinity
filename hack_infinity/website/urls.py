from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    # path('store_data',views.store_data,name='store_data'),
    path('register',views.register,name='register'),    
    # path('index.html',views.index)
    path('login',views.login,name='login'),
    path('logging',views.logging,name='logging'),
    path('logout',views.logout,name='logout'),
    path('inviting',views.inviting,name='inviting'),
    path('create_event',views.create_event,name='create_event'),
    path('create_schedule',views.create_schedule,name='create_schedule'),
    path('show_event_details',views.show_event_details,name='show_event_details'),
    # path('landing_page',views.landing_page,name='landing_page'),
    # path('display_names',views.display_names,name='display_names'),
    # path('send_mail',views.send_mail,name='send_mail'),
    # path('sending_mail',views.sending_mail,name='sending_mail'),

    # path('user_page',views.user_page,name='user_page'),

    
]
