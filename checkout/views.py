# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']
		# Charge the user's card:
		customer = stripe.Customer.retrieve(customer_id)
		customer.sources.create(source=token)
		charge = stripe.Charge.create(
		  amount=1000,
		  currency="usd",
		  description="Example charge",
		  customer=customer,
		)
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request, template, context)
