from django.urls import  path
from .views import index, about, product, pricing, yoga_online, contact, login_user, register_user, logout_user

urlpatterns = [
path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('pricing/', pricing, name='pricing'),
    path('yoga_online/', yoga_online, name='yoga_online'),
    path('contact/', contact, name='contact'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),

    #path('create_product/', create_product, name='create_product')
]