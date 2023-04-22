from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kids/', views.kids_index, name='kids_index'),
    path('kids/<int:kid_id>/', views.kid_detail, name='kid_detail'),

    path('accounts/signup/', views.signup, name='signup')
]