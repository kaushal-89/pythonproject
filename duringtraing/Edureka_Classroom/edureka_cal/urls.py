from django.urls import path, include, re_path
from .views import index, ContactUs, CourseListView, CourseDetailView, SignUpView


urlpatterns = [
    # path('<int:year>/<int:month>/', index, name='flex_cal'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', index, name='flex_cal' ),
    path('', index, name='index'),
    path('contact/', ContactUs.as_view(), name='cotactus'),
    path('course/', CourseListView.as_view(), name = 'course'),
    path('course/<int:pk>', CourseDetailView.as_view(), name = 'course_details'),
]
