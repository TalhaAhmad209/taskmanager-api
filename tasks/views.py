from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer,UserSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # Requires authentication
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Requires authentication
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # Requires authentication
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Requires authentication
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
