from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .froms import UserInfoModelForm
from .models import UserInfo


class Create(CreateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/create.html'
    success_url = reverse_lazy('classbased:list')


class List(ListView):
    template_name = 'classbased/list.html'
    model = UserInfo
    context_object_name = 'data'


class Detail(DetailView):
    template_name = 'classbased/detail.html'
    model = UserInfo
    context_object_name = 'usr_object'
    pk_url_kwarg = 'id'


class Update(UpdateView):
    template_name = 'classbased/update.html'
    form_class = UserInfoModelForm
    pk_url_kwarg = 'id'
    model = UserInfo

    success_url = reverse_lazy('classbased:list')

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass


class Delete(DeleteView):
    model = UserInfo
    success_url = reverse_lazy('classbased:list')
    pk_url_kwarg = 'id'



