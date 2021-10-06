from django.core.mail import get_connection, send_mail
from django.shortcuts import render, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import ContactForm

# Create your views here.

def index(request):
    year = date.today().year
    month = date.today().month

    month_name = calendar.month_name[month]
    title = f"Edureka course calender for {month_name} - {year}"
    cal = HTMLCalendar().formatmonth(year, month)

    return render(request, 'base.html', {'title': title, 'cal': cal})

def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            yourname = cd['yourname']
            message = cd['message']
            subject = cd['subject']
            con = get_connection('django.core.mail.backend.console.EmailBackend')
            send_mail(
            subject,
            message,
                cd.get('email', 'kaushal@gmail.com')
                ['abc@gmail.com'],
                connection=con
            )

            return HttpResponseRedirect('/contact?submitted=False')
    else:
        form = ContactForm()

    return render(request, 'emails/emailform.html', {'form' : form})