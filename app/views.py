from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RequestForm
from .models import Request, Service

class RequestFormView(LoginRequiredMixin, FormView):
    form_class = RequestForm
    template_name = 'request.html'
    success_url = reverse_lazy('form')
    login_url = 'login'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Заявка создана")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Исправьте ошибки")
        return super().form_invalid(form)

class RequestsView(LoginRequiredMixin, ListView):
    model = Request
    template_name = "request2.html"
    context_object_name = "requests"
    paginate_by = 3
    login_url = 'login'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-created_at')

class ServiceListView(ListView):
    model = Service
    template_name = "service.html" 
    context_object_name = "services"