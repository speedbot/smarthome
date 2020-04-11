from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
from .models import Bulb, Fan


class BulbCreateView(LoginRequiredMixin, CreateView):
    model = Bulb
    template_name = 'bulb/create.html'
    fields = ('brightness', 'color', 'owner', 'name', 'state')


class BulbDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulb
    success_url = '/'


class BulbUpdateView(LoginRequiredMixin, UpdateView):
    model = Bulb
    template_name = 'bulb/update.html'
    fields = ('brightness', 'color', 'owner', 'name', 'state')


class BulbDetailView(LoginRequiredMixin, DetailView):
    model = Bulb
    template_name = 'bulb/detail.html'


class FanCreateView(LoginRequiredMixin, CreateView):
    model = Fan
    template_name = 'fan/create.html'
    fields = ('speed', 'owner', 'name', 'state')


class FanDeleteView(LoginRequiredMixin, DeleteView):
    model = Fan
    success_url = '/'

class FanUpdateView(LoginRequiredMixin, UpdateView):
    model = Fan
    template_name = 'fan/update.html'
    fields = ('speed', 'owner', 'name', 'state')


class FanDetailView(LoginRequiredMixin, DetailView):
    model = Fan
    template_name = 'fan/detail.html'


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        bulbs = Bulb.objects.filter(owner=self.request.user)
        fans = Fan.objects.filter(owner=self.request.user)
        ctx = {
            bulbs: bulbs,
            fans: fans,
        }
        return ctx