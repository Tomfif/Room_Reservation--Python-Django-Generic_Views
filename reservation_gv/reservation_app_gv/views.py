import datetime
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from reservation_app_gv.models import ConferenceRoom, RoomReservation


class RoomCreate(CreateView):
    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector_availability']
    success_url = reverse_lazy("room-list")

class RoomListView(ListView):
    template_name = 'rooms.html'
    model = ConferenceRoom

class DeleteRoom(DeleteView):
    template_name = 'delete_room.html'
    success_url = "/"
    model = ConferenceRoom

class ConferenceRoomUpdate(UpdateView):
    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector_availability']
    success_url = "/"



class RoomReservationCreate(CreateView):
    model = RoomReservation
    fields = ['room_id', 'date', 'comment']
    success_url = "/"

class RoomDetailsView(DetailView):
    model = ConferenceRoom
    template_name = 'conferenceroom_details_view.html'
    def get_context_data(self,** kwargs):
        context = super(RoomDetailsView, self).get_context_data(**kwargs)
        context['reservations'] =  self.get_object().roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return context

