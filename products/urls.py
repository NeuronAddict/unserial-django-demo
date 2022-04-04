from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('<int:product_id>/', views.detail, name='detail'),
]
