from django.urls import path
from core.views import index, contact, produto

urlpatterns = [
    path('',index),
    path('contact',contact),
    path('produto/<int:pk>/', produto, name='produto'),  # Exemplo de definição de URL

]