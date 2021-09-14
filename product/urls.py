from django.urls import path
from .views import (ProductsListView, ProductDetailsView, CreateProductView, UpdateProductView,\
                     DeleteProductView)
from .views import ProductViewSet

# urlpatterns = [
#     path('Products/', ProductViewSet.as_view(
#         {'get': 'list'}
#     )),
#     path('Products/<int:pk>/', ProductViewSet.as_view(
#         {'get': 'retrieve'}
#     )),
#     path('Products/create/', ProductViewSet.as_view(
#         {'post': 'create'}
#     )),
#     path('Products/update/<int:pk>/', ProductViewSet.as_view(
#         {'put': 'update', 'patch': 'partial_update'}
#     )),
#     path('Products/delete/<int:pk>/', ProductViewSet.as_view(
#         {'delete': 'destroy'}
#     )),
#
# ]

# urlpatterns = [
#     path('Products/', ProductsListView.as_view()),
#     path('Products/<int:pk>/', ProductDetailsView.as_view()),
#     path('Products/create/', CreateProductView.as_view()),
#     path('Products/update/<int:pk>/', UpdateProductView.as_view()),
#     path('Products/delete/<int:pk>/', DeleteProductView.as_view()),
# ]

urlpatterns = [
    path('Products/', ProductViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('Products/<int:pk>/', ProductViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy',
         }
    ))
    ]
