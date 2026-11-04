from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('students/',views.student_list,name='students'),
    path('search/',views.student_search,name='search'),
    path('add/',views.student_add,name='student_add'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]