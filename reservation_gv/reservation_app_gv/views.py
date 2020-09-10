from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reservation_app_gv.models import ConferenceRoom


class RoomCreate(CreateView):
    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector_availability']
    success_url = reverse_lazy("templates/message")