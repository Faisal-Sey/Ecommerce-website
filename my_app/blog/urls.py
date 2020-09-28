from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ShopDetailsView, ShopListView, OrderSummaryView, CheckoutView, shop, PaymentView, PantsListView, \
    ShirtsListView, ShortsListView, SlippersListView, WatchesListView, PostView, Posts


urlpatterns = [
    path('', views.home, name='home_page'),
    path('shop-grid/', shop.as_view(), name='shop'),
    path('blog/', views.blg, name='blg'),
    path('contact/', views.contact, name='contact'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('blog-details/', views.blg_details, name='blg_details'),
    path('index/', views.index, name='index'),
    path('Shoes/', ShopListView.as_view(), name='Shoes'),
    path('Pants/', PantsListView.as_view(), name='Pants'),
    path('Watches/',WatchesListView.as_view(), name='Watches'),
    path('Slippers/', SlippersListView.as_view(), name='Slippers'),
    path('Shorts/', ShortsListView.as_view(), name='Shorts'),
    path('Shirts/', ShirtsListView.as_view(), name='Shirts'),
    path('login/', views.loginPage, name='login'),
    path('logoutuser/', views.logoutuser, name='logout'),
    path('Signup/', views.Signup, name='Signup'),
    path('posts_list/', views.posts_list, name='posts_list'),
    path('shop-details/<slug>/', ShopDetailsView.as_view(), name='shop-details'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-total-from-cart/<slug>/', views.remove_total_from_cart, name='remove_total_from_cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_from_cart, name='remove_single_from_cart'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('add-item-to-cart/<slug>/', views.add_item_to_cart, name='add_item_to_cart'),
    path('posts', PostView.as_view(), name='posts'),
    path('postsforms', Posts.as_view(), name='postsforms'),
    path('answers', views.answers, name='answers')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)