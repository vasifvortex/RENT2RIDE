from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CartItem, Transaction, Order, OrderItem
from app.models import Cycle
from .serializers import CartItemSerializer, CartItemSerializerAdd
import requests
from django.conf import settings
import stripe

# Create your views here.
@login_required
def cart(request: HttpRequest) -> HttpResponse:
    return render(request, 'cart.html')


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, cycle_id):
        user = request.user
        cycle = get_object_or_404(Cycle, id=cycle_id)
        cart_item = CartItem.objects.get_or_create(user=user, cycle=cycle)
        
        # serializer = CartItemSerializerAdd(cart_item)
        return Response({'message': 'Item added to cart successfully.'}, status=201)

@login_required
def add_to_cart_api(request, cycle_id):
    product = get_object_or_404(Cycle, id=cycle_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if created:
        return JsonResponse({'message': 'Item added to cart successfully.'}, status=201)
    else:
        return JsonResponse({'message': 'Item already exists in cart.'}, status=200)
    
"""
carti local storagede saxla
request atsin user payment ucun cardakilari da gonderir
stripe ile paymente yonlediririk
payment detail db-da saxlanilir
fso
"""
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_amount = sum(item.cycle.price for item in cart_items)
    total_amount_cents = int(total_amount * 100)

    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=total_amount_cents,
            currency='usd',
            metadata={'user_id': user.id}
        )

        # Create a pending order
        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
            status=Order.PENDING,
            stripe_payment_intent_id=payment_intent['id']
        )

        # Create order items
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                cycle=cart_item.cycle,
                quantity=cart_item.quantity,
                price=cart_item.cycle.price
            )

        # Create a pending transaction
        transaction = Transaction.objects.create(
            user=user,
            amount=total_amount,
            status=Transaction.PENDING,
            stripe_payment_intent_id=payment_intent['id']
        )

    except stripe.error.StripeError as e:
        return render(request, 'cart/error.html', {'error': str(e)})

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'client_secret': payment_intent['client_secret'],
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY[0],
    }

    return render(request, 'cart/checkout.html', context)

@login_required
def payment_success(request, payment_intent_id):
    # Retrieve the order and transaction
    order = get_object_or_404(Order, stripe_payment_intent_id=payment_intent_id)
    transaction = get_object_or_404(Transaction, stripe_payment_intent_id=payment_intent_id)
    
    # Update status to accepted
    order.status = Order.ACCEPTED
    transaction.status = Transaction.ACCEPTED
    order.save()
    transaction.save()

    # Clear the user's cart
    CartItem.objects.filter(user=request.user).delete()

    return render(request, 'cart/success.html')


class CartItemListAPIView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user).select_related('cycle')
    
class CartItemDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, cycle_id):
        user = request.user
        cycle = get_object_or_404(Cycle, id=cycle_id)
        cart_item = get_object_or_404(CartItem, user=user, cycle=cycle)
        cart_item.delete()
        
        return Response({'message': 'Item deleted from cart successfully.'}, status=200)