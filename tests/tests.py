from django.test import TestCase


class MiddlewareTest(TestCase):
    def test_middleware(self):
        response = self.client.get('/')

        self.assertEqual(response["Permissions-Policy"], 'interest-cohort=()')
