from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import RegisterForm, BookForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Book


# Create your views here.
def home(request):
    book = Book.objects.all()
    context = {
        'book': book,
    }
    print(context)
    return render(request, 'main/home.html', context)


@login_required(login_url="/login")
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            amount_request = form.save(commit=False)
            amount_request.user = request.user
            amount_request.save()
            messages.success(request, "Book Added Successfully.")
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'main/add_book.html', {'form': form})


def update_book(request):
    book = Book.objects.all()
    context = {
        'book': book,
    }
    print(context)
    return render(request, 'main/update_book.html', context)


@login_required(login_url="/login")
def delete_book(request, id):
    if request.method == "POST":
        pi = Book.objects.get(pk=id)
        pi.delete()
        messages.success(request, "Deleted Successfully.")
        return HttpResponseRedirect('/')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "SignUp Successfully.")
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign.html', {'form': form})


@login_required(login_url="/login")
def update_book_details(request, id):
    if request.method == "POST":
        pi = Book.objects.get(pk=id)
        fm = BookForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Updated Successfully.")
    else:
        pi = pi = Book.objects.get(pk=id)
        fm = BookForm(instance=pi)
    return render(request, 'main/update_book_details.html', {'form': fm})
