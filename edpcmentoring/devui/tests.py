from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

import devui.views as views

class IndexViewTestCase(TestCase):
    fixtures = ['cuedmembers/test_users_and_members']

    def setUp(self):
        self.client = Client()
        self.superuser = get_user_model().objects.filter(
            is_superuser=True, cued_member__isnull=False).first()
        self.url = reverse(views.index)

    def test_index_requires_login(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)

    def test_index_with_login_ok(self):
        self.client.force_login(self.superuser)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_index_uses_template(self):
        self.client.force_login(self.superuser)
        self.client.get(self.url)
        self.assertTemplateUsed('devui/index.html')
