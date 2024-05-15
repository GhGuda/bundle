from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import *
from django.http import HttpRequest
from django.contrib import messages
from django.conf import settings


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
      amount = request.POST['amount']
      gig = request.POST['gig']
      email = request.POST['email']
      number = request.POST['number']
      
      bundle = Bundle.objects.create(amount=amount, gig=gig, email=email, number=number)
      bundle.save()
      return render(request, 'proceed.html', {'pay':bundle, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        return render(request, 'index.html')
    

def proceed(request):
    pass
    return render(request, "proceed.html")


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Bundle, ref=ref)
    verified = payment.verify_payment()
    
    if verified:
        messages.success(request, "Verification Successful")
    else:
        messages.error(request, "Verification failed")
        
    return redirect('index')