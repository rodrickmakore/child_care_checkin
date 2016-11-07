from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from app.models import CustomerProfile, ChildReport
from string import ascii_letters, digits
import random

def new_code():
    char_list = ascii_letters + digits
    code = random.sample(char_list, 4)
    code = "".join(code)
    return code

class IndexView(CreateView):
    model = ChildReport
    fields = ('action',)
    template_name = "index.html"
    success_url = reverse_lazy("index_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.GET:
            context["profile"] = CustomerProfile.objects.get(code=self.request.GET.get("code"))
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.profile = CustomerProfile.objects.get(code=self.request.GET.get("code"))
        return super().form_valid(form)

class CustomerCreateView(CreateView):
    model = CustomerProfile
    fields = ("parent_name", "child_name")
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.code = new_code()
        return super().form_valid(form)

class EmployeeProfileView(TemplateView):
    model = CustomerProfile
    template_name = "profile.html"

class ParentProfileView(DetailView):
    model = CustomerProfile
    success_url = reverse_lazy("parent_profile_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = ChildReport.objects.filter(profile=self.object.id)
        return context
