from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Exam, Task
from .permissions import IsExamOwnerOrReadOnly, IsOwnerOrReadOnly
from .serializers import ExamSerializer, TaskSerializer


class ExamView(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsExamOwnerOrReadOnly)