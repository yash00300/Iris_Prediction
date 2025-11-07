from django.contrib import admin
# blog/admin.py

from django.contrib import admin
from .models import Data

@admin.register(Data)
class PostAdmin(admin.ModelAdmin):
    list_display = ('sepalLengthCm', 'sepalWidthCm', 'petalLengthCm', 'petalWidthCm' ,'species')
    
    

# Register your models here.

