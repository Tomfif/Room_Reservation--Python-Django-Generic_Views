import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView
from reservation_app_gv.models import ConferenceRoom


class RoomCreate(CreateView):
    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector_availability']
    success_url = reverse_lazy("room-list")

class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.roomreservation_set.all()]
            room.reserved = datetime.date.today() in reservation_dates
        return render(request, "rooms.html", context={"rooms": rooms})

class DeleteRoom(DeleteView):
    template_name = 'delete_room.html'
    success_url = '/'
    model = ConferenceRoom