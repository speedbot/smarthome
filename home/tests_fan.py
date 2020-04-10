from django.test import TestCase
from rest_framework.test import APIClient

from .factories import StaffUerFactory
from .models import Fan

class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = StaffUerFactory.create()

    def get_data(self):
        return {
            'owner': self.user.id,
            'name': 'Fan1',
            'state': True,
            'speed': 1,
        }

    def test_create(self):
        self.assertEqual(Fan.objects.count(), 0)
        response = self.client.post('/fan/', self.get_data(), format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Fan.objects.count(), 1)

    def test_create_error(self):
        self.assertEqual(Fan.objects.count(), 0)
        data = self.get_data()
        data['speed']=-1
        response = self.client.post('/fan/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Fan.objects.count(), 0)

    def test_update(self):
        data = self.get_data()
        self.assertEqual(Fan.objects.count(), 0)
        response = self.client.post('/fan/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Fan.objects.count(), 1)
        obj = Fan.objects.first()
        data = self.get_data()
        data['speed'] = 2
        data['state'] = False
        response = self.client.patch('/fan/{}'.format(obj.id), data, format='json')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(Fan.objects.count(), 1)
        response = self.client.get('/fan/{}'.format(obj.id), data, format('json'))

    def test_delete(self):
        self.assertEqual(Fan.objects.count(), 0)
        response = self.client.post('/fan/', self.get_data(), format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Fan.objects.count(), 1)
        obj = Fan.objects.first()

        self.client.delete('/fan/{}/'.format(obj.id))
        self.assertEqual(Fan.objects.count(), 0)


