from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from app.models import Profile, ChildStatus
from string import ascii_letters, digits
import random


def new_code():
    char_list = ascii_letters + digits
    code = random.sample(char_list, 4)
    code = "".join(code)
    return code

class IndexView(TemplateView):
    model = Profile
    fields = ("checked_in",)
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.GET:
            print(self.request.GET)
            context["profile"] = Profile.objects.get(code=self.request.GET.get("code"))
        return context

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #
    #     if self.request.POST.get("checkin"):
    #         instance.checked_in = True
    #     if self.request.POST.get("checkout"):
    #         instance.checked_in = False
    #
    #     return super().form_valid(form)


class ProfileCreateView(CreateView):
    model = Profile
    fields = ("parent_name", "child_name")
    tempalate_name = "create_profile.html"
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.code = new_code()
        return super().form_valid(form)

class ProfileView(TemplateView):
    model = Profile
    template_name = "profile.html"

class StatusCreateView(CreateView):
    model = ChildStatus
    fields = ("status",)

class ParentProfileView(DetailView):
    model = Profile

    # def get_context_data(self):
    #     context = super().get_context_data(**kwargs)
    #     context["transactions"] = ChildStatus.objects.filter(self)
    #     return context
