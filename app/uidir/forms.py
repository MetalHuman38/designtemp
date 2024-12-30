# uidir/forms.py
from django import forms
from uidir.models import Consultation
from uidir.models import Contact


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['fullname', 'email', 'requirements']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 bg-white rounded-md    shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',  # noqa
                'placeholder': 'Your full name',
                'style': 'color: #1a202c;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',  # noqa
                'placeholder': 'Your business email',
                'style': 'color: #1a202c;',
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'form-textarea block w-full px-3 py-2 border border-gray-300 text-gray-900 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',  # noqa
                'placeholder': 'Tell us about your requirements',
                'style': 'color: #1a202c;',
                'rows': 5,
            }),
        }

        def __init__(self, *args, **kwargs):
            super(ConsultationForm, self).__init__(*args, **kwargs)
            self.fields['fullname'].required = True
            self.fields['email'].required = True
            self.fields['requirements'].required = True


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 bg-white rounded-md    shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',  # noqa
                'placeholder': 'Your full name',
                'style': 'color: #1a202c;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',  # noqa
                'placeholder': 'Your business email',
                'style': 'color: #1a202c;',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea block w-full px-3 py-2 border border-gray-300 text-gray-900 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',  # noqa
                'placeholder': 'Your message',
                'style': 'color: #1a202c;',
                'rows': 5,
            }),
        }

        def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['fullname'].required = True
            self.fields['email'].required = True
            self.fields['message'].required = True
