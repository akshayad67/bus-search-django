from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core.mail import send_mail
# Create your views here.

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
	
	for i in stp:
		smalldict=dict()
		smalldict['busname']=(i.busname).encode('ascii', 'ignore')
		smalldict['Busid']=i.Busid
		resul.append(smalldict)
	
	t='chinnuchinnu1959@gmail.com'
	r='akshayad67@gmail.com'	
	send_mail('Test- Bus search Result',str(resul),t, [r],fail_silently=False)


	return JsonResponse(resul,safe=False)
