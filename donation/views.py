from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key="pk_test_51GzQgqCXlb7SRfOrsuiwGPZ6GUP1S2reXQvjNW6vwuPc2jTGsfC1zPVRCPTKOhNkIP7LQxqjjDc6yCno7KIGESIJ00hgKblPeN"

# Create your views here.

def donation(request):
	return render(request, 'donation/donation.html')


def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)
        stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname']
        )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'donation/success.html', {'amount':amount})