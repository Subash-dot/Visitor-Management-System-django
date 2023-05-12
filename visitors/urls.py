from . import views
from django.urls import path


urlpatterns = [
    path("",views.base, name ="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("visitor/",views.visitor, name='visitor'),
    path('new/', views.visitor_create_view, name='visitor_create'),
    path('visitor/checkout/<int:pk>',views.checkout,name="checkout"),
    path('importdata/', views.import_data_to_db,name='import_data_to_db'),
    path('qr/', views.qr, name='qr'),
    path('visitor/details/<int:id>',views.details, name="details"),
    path('visitor/delete/<int:id>',views.delete,name='delete'),
    path('visitor/update/<int:id>',views.update,name='update'),
    path('login/',views.login_user, name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
]