
from django.contrib import admin
from django.urls import path
from collection import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    ]
