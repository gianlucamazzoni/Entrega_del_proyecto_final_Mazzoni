from django.contrib import admin
from .models import Nintendo, Playstation, Xbox, Avatar
# Register your models here.
admin.site.register(Nintendo)

admin.site.register(Playstation)

admin.site.register(Xbox)

admin.site.register(Avatar)