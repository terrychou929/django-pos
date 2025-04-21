from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MenuItem
from django.contrib import messages
import json

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def cart(request):
    cart_items = request.session.get('cart', {})
    items = []
    total = 0
    for item_id, quantity in cart_items.items():
        menu_item = MenuItem.objects.get(id=item_id)
        subtotal = menu_item.price * quantity
        total += subtotal
        items.append({
            'menu_item': menu_item,
            'quantity': quantity,
            'subtotal': subtotal,
        })
    return render(request, 'cart.html', {'cart_items': items, 'total': total})

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        cart = request.session.get('cart', {})
        cart[item_id] = cart.get(item_id, 0) + 1
        request.session['cart'] = cart
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def checkout(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        messages.success(request, '結帳成功！')
        return redirect('menu')
    return redirect('cart')