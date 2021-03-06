"""reservation_gv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reservation_app_gv.views import RoomCreate, RoomListView, DeleteRoom, ConferenceRoomUpdate, RoomReservationCreate

from reservation_app_gv.views import RoomDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addroom/', RoomCreate.as_view(), name="addroom"),
    path('', RoomListView.as_view(), name="room-list"),
    path('deleteroom/<int:pk>/', DeleteRoom.as_view(), name="delete-room"),
    path('modifyroom/<int:pk>/', ConferenceRoomUpdate.as_view(), name="modify-room"),
    path('roomreserve/', RoomReservationCreate.as_view(), name="reservation-room"),
    path('roomdetails/<int:pk>/', RoomDetailsView.as_view(), name="reservation-room"),
]
