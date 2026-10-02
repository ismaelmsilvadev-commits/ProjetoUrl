from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Link


class RedirectUrlViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='tester', password='senha-de-teste')

        self.link = Link.objects.create(url_destination='https://google.com/', url_owner=self.user)

    def test_unknown_code_returns_404(self):
        url = reverse('urlapp:redirect', kwargs={'code': 'nao-existe'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_valid_code_redirects_to_destination(self):
        url = reverse('urlapp:redirect', kwargs={'code': self.link.code})
        response = self.client.get(url)

        # 302, não 301
        self.assertRedirects(response, self.link.url_destination, status_code=302, fetch_redirect_response=False)

    def test_admin_not_captured_by_code_route(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        expected_url = f"{reverse('admin:login')}?next={url}"
        self.assertRedirects(response, expected_url)
