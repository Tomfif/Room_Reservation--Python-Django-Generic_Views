from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class RoomReservation(models.Model):
    room_id = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date',)