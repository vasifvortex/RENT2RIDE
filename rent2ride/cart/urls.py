from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('api/cart/add/<int:cycle_id>', views.AddToCartView.as_view(), name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<payment_intent_id>', views.payment_success, name='payment_success'),
    path('api/cartitems/', views.CartItemListAPIView.as_view(), name='api_cartitems_list'),
    path('api/delete/cartitem/<int:pk>', views.CartItemDeleteAPIView.as_view(), name='api_cartitem_delete'),
]