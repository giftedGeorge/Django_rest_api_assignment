from django.urls import path
from inventory_api.views import List_Computer, Create_Computer, Edit_Computer #create_computer, list_computer, computer

urlpatterns = [
    # path('computers/list', list_computer),
    # path('computers/', create_computer),
    # path('computers/<int:pk>', computer),

    path('computers/list', List_Computer.as_view()),
    path('computers/', Create_Computer.as_view()),
    path('computers/<int:pk>', Edit_Computer.as_view()),
]
