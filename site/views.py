from django.views.generic import TemplateView

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'
