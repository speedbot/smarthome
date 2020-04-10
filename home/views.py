from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
from .models import Bulb, Fan


class BulbCreateView(CreateView):
    model = Bulb
    template_name = 'bulb/create.html'
    fields = ('brightness', 'color', 'owner', 'name', 'state')


class BulbDeleteView(DeleteView):
    model = Bulb


class BulbUpdateView(UpdateView):
    model = Bulb
    template_name = 'bulb/update.html'
    fields = ('brightness', 'color', 'owner', 'name', 'state')


class BulbDetailView(DetailView):
    model = Bulb
    template_name = 'bulb/create.html'


class FanCreateView(CreateView):
    model = Fan
    template_name = 'fan/create.html'
    fields = ('speed', 'owner', 'name', 'state')


class FanDeleteView(DeleteView):
    model = Fan


class FanUpdateView(UpdateView):
    model = Fan
    template_name = 'fan/update.html'
    fields = ('speed', 'owner', 'name', 'state')


class FanDetailView(DetailView):
    model = Fan
    template_name = 'fan/detail.html'


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = {

        }
        return ctx