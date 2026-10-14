from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoginLogoutViewTests(TestCase):
    def setUp(self):
        User = get_user_model()

        self.password = 'senha-teste'
        self.user = User.objects.create_user(username='tester', password=self.password)

    def test_login_page_renders(self):
        url = reverse('userapp:login')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userapp/login.html')

    def test_login_with_valid_credentials_redirects(self):
        url = reverse('userapp:login')

        response = self.client.post(url, {'username': self.user.username, 'password': self.password})

        self.assertRedirects(response, reverse('urlapp:index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_wrong_password_shows_error(self):
        url = reverse('userapp:login')

        response = self.client.post(url, {'username': self.user.username, 'password': 'senhaerradaademais'})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertTrue(response.context['form'].non_field_errors())

    def test_login_respects_next(self):
        url = reverse('userapp:login') + '?next=/admin/'
        response = self.client.post(url, {'username': self.user.username, 'password': self.password})
        next_url = reverse('admin:index')
        self.assertRedirects(response, next_url, fetch_redirect_response=False)

    def test_logout_via_post_logs_out(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('userapp:logout'))

        self.assertRedirects(response, reverse('urlapp:index'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout_via_get_is_not_allowed(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('userapp:logout'))

        self.assertEqual(response.status_code, 405)

        # nova requisição que confirma que a sessão permanece
        # new request confirms the session persists
        
        response = self.client.get(reverse('urlapp:index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
