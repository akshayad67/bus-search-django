from django.contrib import admin

# Register your models here.
from .models import bustab, routetab

myModels = [bustab, routetab]
admin.site.register(myModels)
