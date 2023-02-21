from django.views.generic import TemplateView


class home_view(TemplateView):
    template_name = "homepage.html"
