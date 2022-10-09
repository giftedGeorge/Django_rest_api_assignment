from django.urls import path
from inventory_api.views import List_Computer, Create_Computer, Edit_Computer, List_Mouse, Create_Mouse, Edit_Mouse

urlpatterns = [
    #for the computer entity
    path('computers/list', List_Computer.as_view()),
    path('computers/', Create_Computer.as_view()),
    path('computers/<int:pk>', Edit_Computer.as_view()),

    #for the mouse entity
    path('mouse/list', List_Mouse.as_view()),
    path('mouse/', Create_Mouse.as_view()),
    path('mouse/<int:pk>', Edit_Mouse.as_view()),
]
