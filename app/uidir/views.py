"""
This file contains all views for the app.
"""

from django.contrib import messages
from django.shortcuts import redirect, render
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
            return redirect('home')
    else:
        form = ConsultationForm()

    context = {'form': form}
    return render(request, 'uidir/consultation.html', context)
