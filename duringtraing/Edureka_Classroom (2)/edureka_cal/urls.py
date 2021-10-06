from django.urls import path, include, re_path
from .views import index, ContactUs, CourseListView, CourseDetailView, student_api, HelloView, Instructor_API, Create_Instructor, Instructordetail, Update_Instructor


urlpatterns = [
    # path('<int:year>/<int:month>/', index, name='flex_cal'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', index, name='flex_cal' ),
    path('', index, name='index'),
    path('contact/', ContactUs.as_view(), name='cotactus'),
    path('course/', CourseListView.as_view(), name = 'course'),
    path('course/<int:pk>', CourseDetailView.as_view(), name = 'course_details'),
    path('students/', student_api, name = 'all_students'),
    path("hello/", HelloView.as_view(), name="hello"),
    path('instructor/', Instructor_API.as_view(), name = 'instructor'),
    path('add_instructor/', Create_Instructor.as_view(), name = 'create_instructor'),
    path('instructor/<int:pk>/', Instructordetail.as_view(), name= 'instructor_detail'),
    path('update_instructor/<int:pk>/', Update_Instructor.as_view(), name= 'instructor_update'),
]
