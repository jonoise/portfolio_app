from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(subject=form.cleaned_data['subject'],
                      message=render_to_string('frontend/contact_mail.html', {'name': form.cleaned_data['name'],
                                                                              'email': form.cleaned_data['email'],
                                                                              'message': form.cleaned_data['message']}),
                      from_email='yellowballpython@gmail.com',
                      recipient_list=['amilkarms@outlook.com'],
                      fail_silently=False)
            return redirect('frontend:thankyou')
    context = {
        'form': form,
    }

    return render(request, 'frontend/index.html', context)


def thank_you(request):
    return render(request, 'frontend/thankyou.html')


def portfolio(request):
    return render(request, 'frontend/portfolio.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def next(request):
    return render(request, 'frontend/next.html')
