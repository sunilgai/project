from django.contrib import admin
from .models import Image,Video
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display= ('id','username','email','title','discription','photo','date')

@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display= ('id','username','email','title','discription','video','date')

