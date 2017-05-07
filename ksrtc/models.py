from django.db import models

# Create your models here.

class bustab(models.Model):
	busname=models.CharField(max_length=300)
	Busid=models.IntegerField(default=0)
	def __str__(self):
		return str(self.busname)

class routetab(models.Model):
	stops=models.CharField(max_length=300)
	busob=models.ManyToManyField(bustab)