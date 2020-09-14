import datetime

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from reservation_app_gv.models import ConferenceRoom, RoomReservation


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
    success_url = "/"
    model = ConferenceRoom

class ConferenceRoomUpdate(UpdateView):
    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector_availability']
    template_name_suffix = '_update_form'
    success_url = "/"

class RoomReservationCreate(CreateView):
    model = RoomReservation
    fields = ['room_id', 'date', 'comment']
    success_url = "/"

    # def form_valid(self, form):
    #     ConferenceRoom = form.save(commit=False)
    #     ConferenceRoom.user_id = self.request.user.id
    #     ConferenceRoom.save()
    #     self.success_url = reverse('roomreserve:reservation-room', args=[str(ConferenceRoom.id)])
    #     return super(RoomReservationCreate, self).form_valid(form)