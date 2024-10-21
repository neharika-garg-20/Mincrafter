from django.urls import path
from . import views
urlpatterns = [
   

    path('',views.home),

    path('login/',views.login),

    path('register/',views.register),

    path('profile/',views.profile),

    path('courses/',views.courses),

    path('course_details/',views.course_details),

    path('admin_view/',views.admin_view),

    path('home_unregistered/',views.home_unregistered),

    path('discussion/',views.discussion)
]
