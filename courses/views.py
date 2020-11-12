from django.shortcuts import render
from rest_framework import viewsets
from .models import course
from .serializers import CourseSerializer


class CourseView(viewsets.ModelViewSet):
	queryset = course.objects.all()
	serializer_class = CourseSerializer