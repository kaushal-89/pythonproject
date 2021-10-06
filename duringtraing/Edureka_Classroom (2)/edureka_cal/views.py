from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, get_connection
from django.shortcuts import render, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import ContactForm
from django.views import View
from django.views import generic
from .models import Course, Student
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):

    def get(self, request):
        return Response({'message': "This is my first API in Rest Framework"})


def getcal(month, year):
    return HTMLCalendar().formatmonth(year, month)

@login_required
def index(request, year=date.today().year, month=date.today().month):

    year = int(year)
    month = int(month)
    if year < 1990 or year > 2020:
        year = date.today().year

    month_name = calendar.month_name[month]
    title = f"Edureka course calendar for {month_name} - {year}"

    cal = getcal(month, year)
    #HTMLCalendar().formatmonth(year, month)

    announcements = [
        {'date': '15-09-2020', 'announcement': "Django course registration open"},
        {'date': '25-09-2020', 'announcement': "Django course starts"}
    ]

    return render(request, 'edureka_cal/calendar_base.html', {'title': title, 'cal': cal, 'announcements': announcements})


# def contact(request):
#     submitted = False
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             print(cd)
#             name = cd['yourname']
#             message = cd['message']
#             con = get_connection('django.core.mail.backends.console.EmailBackend')
#             send_mail(
#             cd['subject'],
#             cd['message'],
#             cd.get('email', 'saurabh@django.com'),
#             ['st@django.com'],
#             connection=con)
#
#             return HttpResponseRedirect('/contact?submitted=True')
#
#     else:
#         form = ContactForm()
#         if 'submitted' in request.GET:
#             submitted = True
#
#     return render(request, 'edureka_cal/contact_form.html', {'form': form, 'submitted': submitted})


class ContactUs(View):

    form_class = ContactForm
    template_name = 'edureka_cal/contact_form.html'

    def get(self, request, *args, **kwargs):
        submitted = False
        form = self.form_class()
        if 'submitted' in request.GET:
            submitted = True
        if request.user.is_authenticated:
            print(request.user.username)
        return render(request, self.template_name, {'form': form, 'submitted': submitted, 'message': 'This is done'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            name = cd['yourname']
            message = cd['message']
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
            cd['subject'],
            cd['message'],
            cd.get('email', 'saurabh@django.com'),
            ['st@django.com'],
            connection=con)

            return HttpResponseRedirect('/cal/contact?submitted=True')



class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = '/login/'
    success_message = "%(username)s was created successfully"


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def student_api(request):
    all_students = Student.objects.all()
    return JsonResponse(serializers.serialize("json", all_students), safe=False)


from rest_framework.renderers import JSONRenderer
from .models import Instructor
from .serializer import InstructorSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
# class Instructor_API(APIView):
#
#     def get(self, request):
#         instructor = Instructor.objects.get(id=1)
#         serialized_data = InstructorSerializer(instructor)
#         json = JSONRenderer().render(serialized_data.data)
#         return Response(serialized_data.data)
#     def post(self, request):
#         print(request.POST)
#         json = request.POST
#         stream = io.BytesIO(json)
#         data = JSONParser().parse(stream)
#         serializer_data = InstructorSerializer(data=data)
#         serializer_data.is_valid()
#         print(serializer_data.validated_data)


class Instructor_API(APIView):
    def get(self, request):
        instructors = Instructor.objects.all()
        data = InstructorSerializer(instructors, many=True)
        return Response(data.data)

class Instructordetail(RetrieveDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class Create_Instructor(ListCreateAPIView):

    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class Update_Instructor(RetrieveUpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer