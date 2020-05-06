from django.urls import path
from pages.views import homepage_view
from pages.views import contact_view
from products.views import (product_detail_view, 
    product_create_view, 
    render_initial_data, 
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
    )

app_name = 'products'
urlpatterns = [

    path('', product_list_view, name = 'product-list'),
    path('create/',product_create_view, name='create'),
    path('initial/',render_initial_data, name='initial'),
    path('<int:id>/',dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/',product_delete_view, name='product-delete')
]