from django.test import TestCase


class MiddlewareTest(TestCase):
    def test_not_exists_header(self):
        response = self.client.get('/')
        self.assertEqual(response['Permissions-Policy'], 'browsing-topics=()')

    def test_exists_header(self):
        response = self.client.get('/test_exists')
        self.assertEqual(response['Permissions-Policy'], 'geolocation=*, camera=(), browsing-topics=()')
