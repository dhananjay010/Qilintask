"""qilinproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from qilinapp.views import signUp, signIn, getFoodCategory, getFoodItems, getFoodItemOnAttribute, getPrice, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', signUp , name='signup'),
    path('sign-in/', signIn , name='signin'),
    path('get-food-category/<str:food_category>/', getFoodCategory , name='getFoodCategory'),
    path('get-food-items/<str:food_category>/', getFoodItems , name='getFoodItems'),
    path("get-food-item-on-attribute/<str:food_attribute>/<str:food_category>/", getFoodItemOnAttribute , name='getFoodItemOnAttribute'),
    path("get-food-item-on-attribute/<str:food_attribute>/", getFoodItemOnAttribute , name='getFoodItemOnAttribute'),
    path('get-price/<int:upper_limit>/<int:lower_limit>/', getPrice , name='getPrice'),
    path('search/<str:search_object>/', search , name='search'),
]
