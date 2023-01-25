from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Snack


# Create your views here.
class ThingListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "things"


class ThingDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class ThingUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = "__all__"


class ThingCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class ThingDeleteView(DeleteView):
    template_name = "thing_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")