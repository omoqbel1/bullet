from django.shortcuts import render
from django.http import HttpResponse
from .forms import Customerform
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    return render(request, 'accounts/products.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def thankyou(request):
    return render(request, 'accounts/thankyou.html')

def services(request):
    return render(request, 'accounts/services.html')

def about(request):
    return render(request, 'accounts/about.html')

def quote(request):
    form = Customerform()

    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()

            # Render the template as a string using the form data
            message = render_to_string('accounts/emailquote.html', {'form': form.cleaned_data})

            # Send an email with the rendered template
            send_mail(
                'NEW QUOTE',  # Subject
                message,  # Message
                'wildmagic@zohomail.com',  # From email
                ['wildmagic@zohomail.com', 'dispatch@bulletstransport.com'],  # List of recipients
                fail_silently=False,
                html_message=message  # Set to True to raise an exception if the email fails to send
            )

            # Redirect to the 'thankyou' page
            return redirect('/thankyou/')

    context = {'form':form}
    return render(request, 'accounts/quote.html', context)
