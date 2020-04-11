from django.test import TestCase
from rest_framework.test import APIClient

from .factories import StaffUerFactory
from .models import Bulb


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = StaffUerFactory.create()

    def get_data(self):
        return {
            'owner': self.user.id,
            'name': 'Bulb1',
            'state': True,
            'brightness': 1,
            'color': '#FF0000',
        }

    def test_create(self):
        self.assertEqual(Bulb.objects.count(), 0)
        response = self.client.post('/api/bulb/', self.get_data(), format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Bulb.objects.count(), 1)

    def test_create_error(self):
        self.assertEqual(Bulb.objects.count(), 0)
        data = self.get_data()
        data['brightness']=-1
        response = self.client.post('/api/bulb/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Bulb.objects.count(), 0)

    def test_update(self):
        data = self.get_data()
        self.assertEqual(Bulb.objects.count(), 0)
        response = self.client.post('/api/bulb/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Bulb.objects.count(), 1)
        obj = Bulb.objects.first()
        data = self.get_data()
        data['speed'] = 2
        data['state'] = False
        response = self.client.patch('/api/bulb/{}'.format(obj.id), data, format='json')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(Bulb.objects.count(), 1)
        response = self.client.get('/api/bulb/{}'.format(obj.id), data, format('json'))

    def test_delete(self):
        self.assertEqual(Bulb.objects.count(), 0)
        response = self.client.post('/api/bulb/', self.get_data(), format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Bulb.objects.count(), 1)
        obj = Bulb.objects.first()

        self.client.delete('/api/bulb/{}/'.format(obj.id))
        self.assertEqual(Bulb.objects.count(), 0)


