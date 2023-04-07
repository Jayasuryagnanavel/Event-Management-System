from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('fdp-details/<int:id>/', views.fdp_detail , name="fdp-detail"),
    path('seminar-details/<int:id>/', views.seminar_detail , name="seminar-detail"),
    path('clubevent-details/<int:id>/', views.clubevent_detail , name="clubevent-detail"),
    path('competition-details/<int:id>/', views.competition_detail , name="competition-detail"),
    path('other-details/<int:id>/', views.otherevent_detail , name="otherevent-detail"),
    path('departments/', views.departments, name="departments"),

    path('departments/information-technology/', views.it_department, name="it-department"),
    path('departments/cs-engineering/', views.cs_department, name="cs-department"),
    path('departments/civil-engineering/', views.civil_department, name="civil-department"),
    path('departments/electrical-communication/', views.ec_department, name="ec-department"),
    path('departments/electrical-electronics/', views.ee_department, name="ee-department"),
    path('departments/mechanical-engineering/', views.mech_department, name="mech-department"),

    path('blogs/', views.blogs, name="blog"),

    path('calendar/', views.CalendarView.as_view(), name='calendar')
]
