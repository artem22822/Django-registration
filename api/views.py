import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.views import View

from users.models import Product, Cart, Order, Category

class ApiProductsView(View):
    def get(self,request):
        products = Product.objects.all()
        data = []

        for p in products:
            data.append(p.serialyze)

        print("DFDFDFDFDFDFDFDFDFDFDF")
        print(data)
        return HttpResponse(json.dumps(data))

class ApiProductView(View):
    def get(self,request, product_id):

        try:
            product = Product.objects.get(id=product_id)
            d = {
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'category': product.category.name,
                'id': product_id,
            }
            return JsonResponse(d)

        except Product.DoesNotExist:

            return HttpResponse("Product not found")

class ApiCartView(View):
    def get(self, request, product_id):

        try:
            product = Product.objects.get(id=product_id)
            user = request.user
            cart = Cart.objects.get(user=user)
            cart.products.add(product)
            status ={"status": 'added'}

            return HttpResponse(json.dumps(status))

        except Product.DoesNotExist:

            return HttpResponse("Product not found")

class ApiDeleteItemCart(View):
    def get(self,request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            cart = Cart.objects.get(user=request.user)
            cart.products.remove(product)
            status = {'status': 'deleted'}
            print(product)
            return HttpResponse(json.dumps(status))

        except Product.DoesNotExist:

            return HttpResponse("Product not found")

class ApiSearchView(View):
    def post(self, request):
        search_guery = request.POST.get('api_search','')

        if search_guery:
            products = Product.objects.filter(name__icontains=search_guery)
            data = []
            for product in products:
                data.append({
                                    'name': product.name,
                                    'price': int(product.price),
                                    'description': product.description,
                                    'category': product.category.name,
                                    })

            return HttpResponse(data)

    def get(self,request):
        query_search = request.GET.get('api_search','')
        data = []
        if query_search:

            products = Product.objects.filter(name__icontains=query_search)
            for product in products:
                data.append({
                    'name': product.name,
                    'price': int(product.price),
                    'description': product.description,
                    'category': product.category.name,
                })
        #print(data, "DADADADADADADADADt")
        return HttpResponse(json.dumps(data))

class ApiAddProduct(View):
    def post(self,request):
        print(request.POST)
        r = request.POST
        new_product = Product.objects.create(name=r['name'],
                                             price=r['price'],
                                             description=r['description'],
                                             category_id=r['category']
                                             )

        print(new_product.name,new_product.category, 'NEW PRODUCT')
        new_product.save()
        print(new_product.id)
        return HttpResponse(new_product.id)

class ApiCategoryProducts(View):
    def get(self,request):
        query = request.GET.get('api_category_product', '')
        products = Product.objects.filter(category_id=query)
        data = []
        if products:
            for product in products:
                data.append({
                            'name': product.name,
                            'price': int(product.price),
                            'description': product.description,
                            'category': product.category.name,
                            })

            print(data,"Data")
            return HttpResponse(json.dumps(data))
