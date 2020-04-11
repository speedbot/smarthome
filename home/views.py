from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
from .models import Bulb, Fan


class BulbCreateView(CreateView, LoginRequiredMixin):
    model = Bulb
    template_name = 'bulb/create.html'
    fields = ('brightness', 'color', 'owner', 'name', 'state')


class BulbDeleteView(DeleteView, LoginRequiredMixin):
    model = Bulb


class BulbUpdateView(UpdateView, LoginRequiredMixin):
    model = Bulb
    template_name = 'bulb/update.html'
    fields = ('brightness', 'color', 'owner', 'name', 'state')


class BulbDetailView(DetailView, LoginRequiredMixin):
    model = Bulb
    template_name = 'bulb/detail.html'


class FanCreateView(CreateView, LoginRequiredMixin):
    model = Fan
    template_name = 'fan/create.html'
    fields = ('speed', 'owner', 'name', 'state')


class FanDeleteView(DeleteView, LoginRequiredMixin):
    model = Fan


class FanUpdateView(UpdateView, LoginRequiredMixin):
    model = Fan
    template_name = 'fan/update.html'
    fields = ('speed', 'owner', 'name', 'state')


class FanDetailView(DetailView, LoginRequiredMixin):
    model = Fan
    template_name = 'fan/detail.html'


class Home(TemplateView, LoginRequiredMixin):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        bulbs = Bulb.objects.filter(owner=self.request.user)
        fans = Fan.objects.filter(owner=self.request.user)
        ctx = {
            bulbs: bulbs,
            fans: fans,
        }
        return ctx