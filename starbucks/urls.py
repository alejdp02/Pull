from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('incrementar/<int:item_id>', views.incrementar_valor, name='incrementar_valor'),
    path('decrementar/<int:item_id>', views.decrementar_valor, name='decrementar_valor'),
    path('restocking/<int:item_id>', views.check_needRestocking, name='restocking'),
    path('signin/', views.signin, name='signin'),
    path('logout', views.signout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete/<int:item_id>', views.delete, name='delete'),
]