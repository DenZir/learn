from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

def index(request):
    query = request.GET.get('q')  # Получаем строку поиска из URL
    product_list = Product.objects.all()

    if query:
        product_list = product_list.filter(name__icontains=query)

    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'app/index.html', {
        'products': products,
        'title': 'Каталог товаров',
    })


from django.shortcuts import render

def view_cart(request):
    return render(request, 'app/cart.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'image': product.image.url if product.image else '',
            'quantity': 1,
            'product_id': product.id
        }

    request.session['cart'] = cart
    return redirect('index')

# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = request.session.get('cart', {})

#     if str(product_id) in cart:
#         cart[str(product_id)]['quantity'] += 1
#     else:
#         cart[str(product_id)] = {
#             'name': product.name,
#             'price': float(product.price),
#             'image': product.image.url if product.image else '',
#             'quantity': 1,
#             'product_id': product.id
#         }

#     request.session['cart'] = cart
#     return redirect('index')


# def view_cart(request):
#     cart = request.session.get('cart', {})
#     cart_items = list(cart.values())
#     total_price = sum(item['price'] * item['quantity'] for item in cart_items)

#     return render(request, 'app/cart.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     })


# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', {})

#     if str(product_id) in cart:
#         del cart[str(product_id)]
#         request.session['cart'] = cart

#     return redirect('view_cart')
# def index(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "app/index.html", context=context)
