from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('incrementar/<int:item_id>', views.incrementar_valor, name='incrementar_valor'),
    path('decrementar/<int:item_id>', views.decrementar_valor, name='decrementar_valor'),
    path('signin/', views.signin, name='signin'),
    path('logout', views.signout, name='logout'),
    path('signup/', views.signup, name='signup'),
]