from django.urls import path
from .views import ApiProductsView, ApiProductView, ApiCartView,\
ApiDeleteItemCart, ApiSearchView, ApiAddProduct, ApiCategoryProducts

urlpatterns = [
    path('/products/', ApiProductsView.as_view(), name='api_products'),
    path('/product/<int:product_id>/', ApiProductView.as_view(), name='api_product'),
    path('/cart/<int:product_id>/', ApiCartView.as_view(), name='api_product'),
    path('/cartdel/<int:product_id>/', ApiDeleteItemCart.as_view(), name='api_cartdel'),
    path('/search/', ApiSearchView.as_view(), name='api_search'),
    path('/addproduct/', ApiAddProduct.as_view(), name='api_add_product'),
    path('/categoryproduct/', ApiCategoryProducts.as_view(), name='api_category_product'),
]