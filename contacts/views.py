from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework import permissions

class ContactList(ListCreateAPIView):

    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class ContactDetailView(RetrieveDestroyAPIView):

    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)