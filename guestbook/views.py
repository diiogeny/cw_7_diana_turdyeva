from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import GuestbookEntry
from .forms import SearchForm
from .forms import GuestbookForm

def index(request):
    search_form = SearchForm(request.GET or None)
    query = request.GET.get('search', '')

    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookForm()

    if query:
        entries = GuestbookEntry.objects.filter(author_name__icontains=query)
    else:
        entries = GuestbookEntry.objects.all()

    return render(request, 'guestbook/index.html', {
        'search_form': search_form,
        'form': form,
        'entries': entries,
    })


def add_entry(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookForm()
    return render(request, 'guestbook/add_edit.html', {'form': form, 'title': 'Добавить запись'})

def edit_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        form = GuestbookForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookForm(instance=entry)
    return render(request, 'guestbook/add_edit.html', {'form': form, 'title': 'Редактировать запись'})

def delete_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        input_email = request.POST.get('email')
        if entry.email and input_email == entry.email:
            entry.delete()
            messages.success(request, "Запись удалена.")
            return redirect('index')
        else:
            messages.error(request, "Email не совпадает или отсутствует.")
    return render(request, 'guestbook/confirm_delete.html', {'entry': entry})



