from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Customerform
from django.core.mail import EmailMessage  # We use EmailMessage now
from django.template.loader import render_to_string
import re


# Simple email and phone regex for server-side check
EMAIL_REGEX = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
PHONE_REGEX = re.compile(r'^\+?\d{7,15}$')

# Create your views here.

def privacy(request):
    return render(request, 'accounts/privacy.html')

def tos(request):
    return render(request, 'accounts/tos.html')

def home(request):
    return render(request, 'accounts/dashboard.html')

def forms(request):
    return render(request, 'accounts/forms.html')

def contact(request):
    return render(request, 'accounts/contact.html')

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
    if request.method == 'POST':
        # Common final-step fields
        category        = request.POST.get('category', '').strip()
        pickup_address  = request.POST.get('pickup_address', '').strip()
        dropoff_address = request.POST.get('dropoff_address', '').strip()
        timeframe       = request.POST.get('timeframe', '').strip()
        custom_date     = request.POST.get('custom_date', '').strip()
        full_name       = request.POST.get('full_name', '').strip()
        phone_number    = request.POST.get('phone_number', '').strip()
        email_address   = request.POST.get('email_address', '').strip()

        # Cars
        car_year     = request.POST.get('car_year', '').strip()
        car_make     = request.POST.get('car_make', '').strip()
        car_model    = request.POST.get('car_model', '').strip()
        car_type     = request.POST.get('car_type', '').strip()
        car_operable = request.POST.get('car_operable', '').strip()

        # Motorcycles
        moto_year     = request.POST.get('moto_year', '').strip()
        moto_make     = request.POST.get('moto_make', '').strip()
        moto_model    = request.POST.get('moto_model', '').strip()
        moto_operable = request.POST.get('moto_operable', '').strip()

        # Boats
        boat_year               = request.POST.get('boat_year', '').strip()
        boat_make               = request.POST.get('boat_make', '').strip()
        boat_model              = request.POST.get('boat_model', '').strip()
        boat_on_trailer         = request.POST.get('boat_on_trailer', '').strip()
        boat_trailer_roadworthy = request.POST.get('boat_trailer_roadworthy', '').strip()

        # Containers
        container_size   = request.POST.get('container_size', '').strip()
        container_assist = request.POST.get('container_assist', '').strip()
        container_weight = request.POST.get('container_weight', '').strip()

        # Freight
        freight_type   = request.POST.get('freight_type', '').strip()
        ltl_unit_type  = request.POST.get('ltl_unit_type', '').strip()
        ltl_weight     = request.POST.get('ltl_weight', '').strip()
        ftl_length     = request.POST.get('ftl_length', '').strip()
        ftl_weight     = request.POST.get('ftl_weight', '').strip()

        # Heavy Equipment
        heavy_make     = request.POST.get('heavy_make', '').strip()
        heavy_model    = request.POST.get('heavy_model', '').strip()
        heavy_year     = request.POST.get('heavy_year', '').strip()
        heavy_weight   = request.POST.get('heavy_weight', '').strip()
        heavy_operable = request.POST.get('heavy_operable', '').strip()

        # Generic
        subcategory   = request.POST.get('subcategory', '').strip()
        item_details  = request.POST.get('item_details', '').strip()

        # File attachments (Step 3)
        uploaded_files = request.FILES.getlist('images')

        # Server-side checks
        if not full_name:
            return render(request, 'accounts/quote.html', {
                'error': 'Your name is required.'
            })
        if not pickup_address:
            return render(request, 'accounts/quote.html', {
                'error': 'Pickup address is required.'
            })
        if not dropoff_address:
            return render(request, 'accounts/quote.html', {
                'error': 'Dropoff address is required.'
            })
        if not phone_number or not PHONE_REGEX.match(phone_number):
            return render(request, 'accounts/quote.html', {
                'error': 'Invalid or missing phone number.'
            })
        if not email_address or not EMAIL_REGEX.match(email_address):
            return render(request, 'accounts/quote.html', {
                'error': 'Invalid or missing email address.'
            })

        # Build context for the email
        context = {
            'category': category,
            'pickup_address': pickup_address,
            'dropoff_address': dropoff_address,
            'timeframe': timeframe,
            'custom_date': custom_date,
            'full_name': full_name,
            'phone_number': phone_number,
            'email_address': email_address,

            # Cars
            'car_year': car_year,
            'car_make': car_make,
            'car_model': car_model,
            'car_type': car_type,
            'car_operable': car_operable,

            # Motorcycles
            'moto_year': moto_year,
            'moto_make': moto_make,
            'moto_model': moto_model,
            'moto_operable': moto_operable,

            # Boats
            'boat_year': boat_year,
            'boat_make': boat_make,
            'boat_model': boat_model,
            'boat_on_trailer': boat_on_trailer,
            'boat_trailer_roadworthy': boat_trailer_roadworthy,

            # Containers
            'container_size': container_size,
            'container_assist': container_assist,
            'container_weight': container_weight,

            # Freight
            'freight_type': freight_type,
            'ltl_unit_type': ltl_unit_type,
            'ltl_weight': ltl_weight,
            'ftl_length': ftl_length,
            'ftl_weight': ftl_weight,

            # Heavy Equipment
            'heavy_make': heavy_make,
            'heavy_model': heavy_model,
            'heavy_year': heavy_year,
            'heavy_weight': heavy_weight,
            'heavy_operable': heavy_operable,

            # Generic
            'subcategory': subcategory,
            'item_details': item_details,
        }

        # Render the email
        html_message = render_to_string('accounts/emailquote.html', context)

        # Construct & send email
        email_msg = EmailMessage(
            subject='NEW QUOTE',
            body=html_message,
            from_email='wildmagic@zohomail.com',
            to=['wildmagic@zohomail.com', 'dispatch@bulletstransport.com']
        )
        email_msg.content_subtype = 'html'

        # Attach any images
        for f in uploaded_files:
            email_msg.attach(f.name, f.read(), f.content_type)

        email_msg.send(fail_silently=False)

        return redirect('/thankyou/')

    # GET request → render blank form
    return render(request, 'accounts/quote.html')
