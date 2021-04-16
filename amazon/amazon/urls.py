"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('product',views.ModelViewset,basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('category/',views.category,name='category'),
    path('cat_product/<int:cat_id>/',views.categoryproduct,name='cat_product'),
    path('brand/',views.brand,name='brand'),
    path('brand_product/<int:brand_id>/',views.brandproduct,name='brand_product'),
    path('product_detail/<int:id>',views.product_detail,name='product_detail'),
    path('cart_add/<int:pro_id>/',views.AddCartView.as_view(),name='cart_add'),
    path('mycart/',views.MyCartView.as_view(),name='mycart'),
    path('managecart/<int:cp_id>/',views.ManageCartView.as_view(),name='managecart'),
    path('empty',views.EmptyCart.as_view(),name='empty'),
    path('checkout/',views.CheckoutView.as_view(),name='checkout'),

    path('products_list/',views.products_list,name='products_list'),
    path('products_detail/<int:pk>/',views.products_detail,name='products_detail'),

    path('products_lists/',views.ProductListView.as_view(),name='products_lists'),
    path('products_details/<int:id>/',views.ProductDetailView.as_view(),name='prooducts_details'),
    path('product_generic/<int:id>/',views.GenericApiView.as_view(),name='product_generic'),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
