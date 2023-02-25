from django.urls import path
from .import views
from .views import HomeView, SingupView, LoginView, LogoutView, \
ProductView, AddToCart, CartView, DeleteItemCart, ViewProduct,OrderView, MyOrdersView ,\
CategoryView, ViewCategoryView

urlpatterns = [
    path('', SingupView.as_view(), name='singup'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('product/', ProductView.as_view(), name='product'),
    path('cart/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('card/', CartView.as_view(), name='card_page'),
    path('cart/remove/<int:item_id>/', DeleteItemCart.as_view(), name='delete_item_card'),
    path('product/viwe/<int:product_id>/', ViewProduct.as_view(), name='viwe_product'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('myorders/', MyOrdersView.as_view(), name='my_orders'),
    path('category/', CategoryView.as_view(), name='category'),
    path('viwecategory/<int:category_obj>/', ViewCategoryView.as_view(), name='view_category'),

]