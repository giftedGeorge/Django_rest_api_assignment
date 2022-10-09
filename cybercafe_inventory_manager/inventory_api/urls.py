from django.urls import path
from inventory_api.views import List_Computer, Create_Computer, Edit_Computer, List_Mouse, Create_Mouse, Edit_Mouse, List_Keyboards, Create_Keyboard, Edit_Keyboard, List_Monitors, Create_Monitor, Edit_Monitor

urlpatterns = [
    #for the computer entity
    path('computers/list', List_Computer.as_view()),
    path('computers/', Create_Computer.as_view()),
    path('computers/<int:pk>', Edit_Computer.as_view()),

    #for the mouse entity
    path('mouse/list', List_Mouse.as_view()),
    path('mouse/', Create_Mouse.as_view()),
    path('mouse/<int:pk>', Edit_Mouse.as_view()),

    #for the keyboard entity
    path('keyboards/list', List_Keyboards.as_view()),
    path('keyboards/', Create_Keyboard.as_view()),
    path('keyboards/<int:pk>', Edit_Keyboard.as_view()),

    #for the monitor entity
    path('monitors/list', List_Monitors.as_view()),
    path('monitors/', Create_Monitor.as_view()),
    path('monitors/<int:pk>', Edit_Monitor.as_view()),
]
