from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView

from .models import Link


class RedirectUrlView(RedirectView):
    # HTTP 302
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        # receives the redirect code
        code = self.kwargs['code']

        url_object = get_object_or_404(Link, code=code)

        return url_object.url_destination

class IndexView(TemplateView):
    template_name = 'urlapp/index.html'

   