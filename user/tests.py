# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Register
# # Create your tests here.
# class registerTest(APITestCase):
#     def test_register(self):
#         response = self.client.post('/register/', {
#             'name': 'sai',
#             'email': 'hassamafridi14@gmail.com', 
#             'password': '12345',
#             'mobile': '123456789'
#         })
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.json(), {'message': 'User added successfully'})
#         self.assertEqual(response.json(), {'message': 'User added successfully'})