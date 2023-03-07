from django.shortcuts import render
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer


class ExamView():
    queryset = Exam.objects.all()
    serializers_class = ExamSerializer


class TaskView():
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
