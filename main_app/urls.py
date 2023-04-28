from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kids/', views.kids_index, name='kids_index'),
    path('kids/<int:kid_id>/', views.kid_detail, name='kid_detail'),

    path('kids/create/', views.KidCreate.as_view(), name='kid_create'),
    path('kids/<int:pk>/update', views.KidUpdate.as_view(), name='kid_update'),
    path('kids/<int:pk>/delete/', views.KidDelete.as_view(), name='kid_delete'),
    path('kids/<int:kid_id>/add_event/', views.add_event, name='add_event'),
    path('kids/<int:kid_id>/add_photo/', views.add_photo, name='add_photo'),

    path('accounts/signup/', views.signup, name='signup')
]