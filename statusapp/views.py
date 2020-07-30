from django.shortcuts import render
from django.views.generic import CreateView, DeleteView

from .forms import StatusMessageModelFOrm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import StatusMessage

@method_decorator(login_required, name='dispatch')
class StatusMessageCreateView(CreateView):
    form_class = StatusMessageModelFOrm
    template_name = 'statusapp/create.html'
    success_url = reverse_lazy('account:profile')

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class StatusMessageDelete(DeleteView):
    model = StatusMessage
    success_url = reverse_lazy('account:profile')

    def get_queryset(self):
        return StatusMessage.objects.filter(
            user=self.request.user
        )

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)