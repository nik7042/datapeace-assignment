from django.urls import path
from .views import UserDetailView,UserListCreateView

urlpatterns = [
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
]

