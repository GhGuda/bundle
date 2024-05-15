from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proceed", views.proceed, name="proceed"),
    path("verify_payment/<str:ref>", views.verify_payment, name="verify-payment"),
    
]
