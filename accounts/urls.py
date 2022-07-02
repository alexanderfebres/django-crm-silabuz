from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("products/", views.products, name="products"),
    path("customer/<str:pk>/", views.customer, name="customer"),
    # ------------ (CREATE URLS) ------------
    path("create_order/", views.create_order, name="create_order"),
    # ------------ (UPDATE URLS) ------------
    path("update_order/<str:pk>/", views.update_order, name="update_order"),
    # ------------ (UPDATE URLS) ------------
    path("delete_order/<str:pk>/", views.delete_order, name="delete_order"),
]
