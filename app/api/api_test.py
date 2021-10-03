import os
from django.contrib.staticfiles.testing import LiveServerTestCase
from rest_framework.test import RequestsClient

"""
API testing
run me with `python manage.py test api.api_test.APITests`
"""


class APITests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        if 'TEST_URL' in os.environ:
            cls.live_server_url = os.environ['TEST_URL']
        else:
            super(APITests, cls).setUpClass()
        cls.client = RequestsClient()

    @classmethod
    def tearDownClass(self):
        if 'TEST_URL' not in os.environ:
            super().tearDownClass()

    def test_01_new_point(self):
        response = self.client.post('{}/api/points/'.
                                    format(self.live_server_url),
                                    {
                                            'element_name': 'Chateau',
                                            'longitude': 2.1348425745964055,
                                            'latitude': 48.70333168603693,
                                            'comment': '',
                                            'date': '2019-10-01'
                                        },
                                    format='json'
                                    )
        self.assertEqual(response.status_code, 201)
        point_id = response.data['id']
        response = self.client.get('{}/api/points/{}/'.
                                   format(self.live_server_url, point_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'id': point_id,
            'element_name': 'Chateau',
            'longitude': 2.1348425745964055,
            'latitude': 48.70333168603693,
            'comment': '',
            'date': '2019-10-01'
        })

    def test_02_delete_point(self):
        response = self.client.post('{}/api/points/'.
                                    format(self.live_server_url),
                                    {
                                            'element_name': 'Chateau',
                                            'longitude': 2.1348425745964055,
                                            'latitude': 48.70333168603693,
                                            'comment': '',
                                            'date': '2019-10-01'
                                        },
                                    format='json'
                                    )
        point_id = response.data['id']
        response = self.client.delete('{}/api/points/{}/'.
                                      format(self.live_server_url, point_id))
        self.assertEqual(response.status_code, 204)
        response = self.client.get('{}/api/points/{}/'.
                                   format(self.live_server_url, point_id))
        self.assertEqual(response.status_code, 404)
