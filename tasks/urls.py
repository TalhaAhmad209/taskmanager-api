from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView,RegisterView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),  # Obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  # Refresh JWT token
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('register/', RegisterView.as_view(), name='register'),
]
