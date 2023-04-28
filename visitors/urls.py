from . import views
from django.urls import path

urlpatterns = [
    path("",views.base, name ="index"),
    path("test/", views.test, name='test'),
    path("newvisitor/",views.newVisitor, name='newvisitor')
]