from django.contrib.auth.models import *
from rest_framework import serializers
from models import *


class bustabSerializer(serializers.ModelSerializer):
	class Meta:
		model = bustab
		fields = ('id', 'busname', 'Busid')

class routetabSerializer(serializers.ModelSerializer):
	busob= bustabSerializer()
	class Meta:
		model = routetab
		fields = ('id', 'stops', 'busob')