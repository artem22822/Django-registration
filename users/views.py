import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from users.models import Product, Cart, Order, Category


class HomeView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        return render(request, 'accounts/home.html')

class SingupView(View):
    def get(self,request):
        return  render(request, 'accounts/index.html')

    def post(self,request):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse('You Password mismatch !!!')
        else:
            user = User.objects.create_user(uname,email,password1)
            user.save()
            print(uname, email, password1)
            return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect!!!!!')

class LogoutView(View):
    def get(self,reques):
        logout(reques)
        return redirect('login')

class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        cart = request.session.get('cart', {})
        context = {
            'products': products,
            'cart': cart,
        }
        return render(request, 'accounts/product.html', context)

class AddToCart(View):
    def post(self,request, product_id):
        product = Product.objects.get(id=product_id)
        user = request.user

        cart, created = Cart.objects.get_or_create(user=user)


        if request.method == 'POST':
            print(product, product.name, product.price, product.description)
            print(user.username)
            cart.products.add(product)
            print(cart)
            return redirect('card_page')

class CartView(View):
    def get(self,request):
        card = Cart.objects.get(user=request.user)
        return render(request, 'accounts/cart.html', context={'card': card})

class DeleteItemCart(View):
    def post(self,request, item_id):
        product = get_object_or_404(Product, id=item_id)
        cart = Cart.objects.get(user=request.user)

        if request.method == 'POST':
            cart.products.remove(product)
            return redirect('card_page')

class ViewProduct(View):
    def get(self,request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'accounts/viwe_product.html', context={'x': product})

class OrderView(View):
    def post(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        total_price = Cart.total_price(cart)
        delivery_addres = request.POST.get('delivery_addres')
        products = list(cart.products.all())
        print(products, "PRODACTSSSSSS")

        order = Order.objects.create(user=user, total_price=total_price, delivery_addres=delivery_addres)
        order.products.add(*products)
        order.save()

        context = {
            'user': user,
            'order' : cart,
            'total_price' : total_price

        }

        return render(request, 'accounts/orders.html', context=context)

class MyOrdersView(View):
    def get(self,request):
        user = request.user
        orders = Order.objects.filter(user=user)
        print(orders)

        return render(request, 'accounts/my_orders.html', context={'orders': orders})

class CategoryView(View):
    def get(self,request):
        category = Category.objects.all()
        return render(request, 'accounts/category.html',context={'category':category})

class ViewCategoryView(View):
    def get(self,request, category_obj):
        category_object = Category.objects.get(id=category_obj)
        product_category = Product.objects.filter(category=category_object)

        print(product_category,'Categor1111')
        print(category_object, 'Id category')
        context = {
            'category_obj': category_object,
            'product_category': product_category,
        }

        return render(request, 'accounts/view_category.html', context=context)

class ProductSearchView(View):
    def post(self, request):
        search_guery = request.POST.get('search','')
        if search_guery:
            products = Product.objects.filter(name__icontains=search_guery)
            print(products)

            return render(request, 'accounts/product.html', context={'products': products})
        else:

            return render(request, 'accounts/home.html')

class RenderJsView(View):
    def get(self,request):
        return render(request, 'accounts/render_js.html')