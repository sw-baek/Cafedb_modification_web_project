from django.urls import path
from . import views

app_name = 'edit'

urlpatterns = [
    # path('shoplist/', views.shop_list, name='shop_list'),
    path('detail/<int:geocafe_id>', views.shop_detail, name='shop_detail'),
    # path('delete/<int:geocafe_id>', views.shop_delete, name='shop_delete'),
    path('update/<int:geocafe_id>', views.shop_update, name='shop_update'),

    path('test/', views.test, name='test'),
]
