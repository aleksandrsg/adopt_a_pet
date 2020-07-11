from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key="sk_test_51GzQgqCXlb7SRfOrHopPuVmW8OjuVHBg9lHTHLs7wvIE1YNlvhH3YRCixIL6k0m6FizCxd0HoikGx6XD1kbyl5Ml00pLUSwAoL"

# Create your views here.

def donation(request):
	return render(request, 'donation/donation.html')


def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = 500,
            currency ='eur',
            description = "Donation"
        )
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'donation/success.html', {'amount':amount})