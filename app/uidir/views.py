"""
This file contains all views for the app.
"""

from django.contrib import messages
from django.shortcuts import redirect, render
from uidir.forms import ContactForm
from uidir.forms import ConsultationForm


def home(request):
    """
    Home page view
    """

    form = ConsultationForm()

    return render(request, 'uidir/home.html', {'form': form})


def consultation(request):
    """
    This view handles the
    consultation form submission.
    """

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you for your consultation request! We'll be in touch soon."
            )
            return redirect('uidir:home')
    else:
        form = ConsultationForm()

    context = {'form': form}
    return render(request, 'uidir/consultation.html', context)


def contact(request):
    """
    Handles contact form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you for your message! We'll be in touch soon."
            )
            return redirect('uidir:home')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'uidir/contact.html', context)


def profile(request):
    """
    About page view
    """

    return render(request, 'uidir/profile.html')


def services(request):
    """
    Services page view
    """

    form = ContactForm()

    return render(request, 'uidir/services.html', {'form': form})
