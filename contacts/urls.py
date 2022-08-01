from django.urls import path
from  contacts import views

urlpatterns=[
    path('',views.ContactList.as_view()),
    path('<int:id>',views.ContactDetailView.as_view())
]