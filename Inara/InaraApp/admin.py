from django.contrib import admin
from .models import Ships, Commander, Station, User
# Register your models here.
admin.site.register(Ships)
admin.site.register(Commander)
admin.site.register(Station)
admin.site.register(User)