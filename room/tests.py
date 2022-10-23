from urllib import response
from django.test import TestCase
from room.models import Room, BookingDetail
import datetime
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Create your tests here.


class get_room_test(APITestCase):
    def setUp(self) -> None:
        Room.objects.create(id=1, room_no=1, room_type='single-bed',price=1000, is_available=True, day=datetime.date.today())
        Room.objects.create(id=2, room_no=2, room_type='duble-bed',price=2000, is_available=True, day=datetime.date.today())

    def test_get_room(self):
        url = reverse('room-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_room_detail(self):
        url = reverse('Room-Detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['room_no'], '1')

    def test_get_room_detail_not_found(self):
        url = reverse('Room-Detail', kwargs={'pk': 3})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_room_no(self):
        room1 = Room.objects.get(room_no='1')
        room2 = Room.objects.get(room_no='2')
        self.assertEqual(room1.room_no, '1')
        self.assertEqual(room2.room_no, '2')

    def test_room_type(self):
        room1 = Room.objects.get(room_no='1')
        room2 = Room.objects.get(room_no='2')
        self.assertEqual(room1.room_type, 'single-bed')
        self.assertEqual(room2.room_type, 'duble-bed')

    def test_price(self):
        room1 = Room.objects.get(room_no='1')
        room2 = Room.objects.get(room_no='2')
        self.assertEqual(room1.price, 1000)
        self.assertEqual(room2.price, 2000)


class BookingDetailTest(APITestCase):
    def setUp(self) -> None:
        self.room1 = Room.objects.create(
            id=1, room_no=1, room_type='single-bed', price=1000, is_available=True, day=datetime.date.today())
        self.room2 = Room.objects.create(
            id=2, room_no=2, room_type='duble-bed', price=2000, is_available=True, day=datetime.date.today())
        self.booking1 = BookingDetail.objects.create(room=self.room1, check_in="2022-02-23", check_out="2022-02-25", no_of_guests=2, total_price=2000)
        self.booking2 = BookingDetail.objects.create(room=self.room2, check_in="2022-02-26", check_out="2022-02-27", no_of_guests=2, total_price=2000)

    def test_same_room_no_booking(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-02-23",
            "check_out": "2022-02-25",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_get_booking_detail(self):
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    

    def test_create_booking_detail(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-01-23",
            "check_out": "2022-01-25",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['room']['id'], 1)

    def test_create_duplicate_booking(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-02-21",
            "check_out": "2022-02-23",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_booking_conflict(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-02-23",
            "check_out": "2022-02-25",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_booking_before(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-01-23",
            "check_out": "2022-01-25",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['room']['id'], 1)

    def test_create_booking_after(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-03-23",
            "check_out": "2022-03-25",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['room']['id'], 1)

    def test_create_booking_between(self):
        url = f"/api/room/{self.room1.pk}/booking/create/"
        data = {
            "check_in": "2022-02-24",
            "check_out": "2022-02-24",
            "no_of_guests": 2,
            "total_price": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

