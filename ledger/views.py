from functools import reduce
from operator import attrgetter

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, DeleteView

from ledger.forms import NewSingleEntryForm
from ledger.models import SingleEntry


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'ledger/index.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return SingleEntry.objects.all()


class SummaryView(LoginRequiredMixin, ListView):
    template_name = 'ledger/summary.html'
    context_object_name = 'context'

    def get_queryset(self, **kwargs):
        context = summarize_users()
        return context


def summarize_users():
    ret = {}
    for user in User.objects.all():
        ret[user] = reduce(lambda x, y: x + y, map(attrgetter('price'), SingleEntry.objects.filter(paid_by=user)))
    return ret


def post_new_single_entry(request):
    if request.method == "POST":
        form = NewSingleEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.paid_by = request.user
            entry.date = timezone.now()
            entry.save()
            return redirect('index')
    else:
        form = NewSingleEntryForm()
    return render(request, 'ledger/entry_edit.html', {'form': form})


def edit_single_entry(request, pk):
    entry = get_object_or_404(SingleEntry, pk=pk)
    if request.method == "POST":
        form = NewSingleEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.paid_by = request.user
            entry.date = timezone.now()
            entry.save()
            return redirect('index')
    else:
        form = NewSingleEntryForm(instance=entry)
    return render(request, 'ledger/entry_edit.html', {'form': form})


class EntryUpdateForm(CreateView):
    model = SingleEntry
    form_class = NewSingleEntryForm
    template_name = 'ledger/entry_edit.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.date = timezone.now()
        form.instance.paid_by = self.request.user
        return super(EntryUpdateForm, self).form_valid(form)


class EntryDeleteForm(DeleteView):
    model = SingleEntry
    success_url = reverse_lazy('index')
    template_name = 'ledger/entry_delete.html'
