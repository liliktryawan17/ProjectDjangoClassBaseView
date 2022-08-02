from django.db.models import QuerySet
from django.views.generic import TemplateView

from artikel.views import ArtikelCategory


class HomeView(TemplateView, ArtikelCategory):
    template_name = "index.html"

    def get_context_data(self):
        querysets = self.get_artikel_category()
        context = {
            'lates_artikel': querysets
        }

        return context
