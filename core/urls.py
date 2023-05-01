from django.urls import path
from .views import index, contato, produto, produtos


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produtos', produtos, name='produtos'),
    path('<int:id>/produto', produto, name='produto'),
]
