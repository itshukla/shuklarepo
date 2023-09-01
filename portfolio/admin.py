from django.contrib import admin
from .models import *



@admin.register(users)
class userAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']
# Register your models here.
