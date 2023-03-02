from django.urls import path
from .views import ApiProductsView, ApiProductView, ApiCartView,\
ApiDeleteItemCart, ApiSearchView, ApiAddProduct, ApiCategoryProducts

urlpatterns = [
    path('api/products/', ApiProductsView.as_view(), name='api_products'),
    path('api/product/<int:product_id>/', ApiProductView.as_view(), name='api_product'),
    path('api/cart/<int:product_id>/', ApiCartView.as_view(), name='api_product'),
    path('api/cartdel/<int:product_id>/', ApiDeleteItemCart.as_view(), name='api_cartdel'),
    path('api/search/', ApiSearchView.as_view(), name='api_search'),
    path('api/addproduct/', ApiAddProduct.as_view(), name='api_add_product'),
    path('api/categoryproduct/', ApiCategoryProducts.as_view(), name='api_category_product'),
]