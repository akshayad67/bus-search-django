from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.models import *
from ksrtc.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()

def result(request,src,des):
	stp=[ ]
	resul=[ ]
	srce= routetab.objects.filter(stops=src)
	print srce
	desti=routetab.objects.filter(stops=des)
	print desti
	z=srce[0].busob.all()
	x=desti[0].busob.all()
	for i in z:
		for j in x:
			if(i==j):
				stp.append(i)

	serializer= bustabSerializer(stp,many=True)
	
	t='akshayad67@gmail.com'
	r='akshayad.mec@gmail.com'	
	send_mail('Test- Bus search Result',str(stp),t, [r],fail_silently=False)


	return Response(serializer.data)