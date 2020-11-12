from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = course
		fields = ('id','url', 'name', 'language','price')

	
	
		