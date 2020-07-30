from django.http import HttpResponse
from django.shortcuts import render

from django.views import View


# Create your views here.
from django.views.generic import TemplateView, RedirectView


class FirstView(View):
    # get function, post function

    def get(self, request, *args, **kwargs):
        return HttpResponse("Get called")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Post called")


class FirstTemplate(TemplateView):
    template_name = 'classbased/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context", context)
        context["msg"] = "HelloWOlrd"
        return context


class FirstRedirectTemplate(RedirectView):
    url = "/c/first/"