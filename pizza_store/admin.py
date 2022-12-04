from django.contrib import admin
from .models import Pizza, Size, Swallow

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Size)
admin.site.register(Swallow)
